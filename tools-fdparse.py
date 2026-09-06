import re, os, glob
from collections import Counter

FD_DIR = 'SRC/FD'
OUT    = 'SCHEMA.md'

hdr_re  = re.compile(r'^\s*(RECORD|COMMON|GROUP)\b\s*(\S+)?\s*(?:;\s*(.*))?$', re.I)
fld_re  = re.compile(r"^\s+(\w+)?\s*,\s*(\d*[A-Za-z]\d+(?:\.\d+)?)\s*"
                     r"(?:,\s*'([^']*)')?\s*(?:;\s*(.*))?$")
dir_re  = re.compile(r'^\s*\.(IFDEF|IFNDEF|ELSE|ENDC|INCLUDE|END)\b\s*(\S+)?', re.I)
size_re = re.compile(r'^(\d*)([A-Za-z])(\d+)')
tail_re = re.compile(r'\s+([A-Za-z]\d+(?:\.\d+)?)\s*$')

def width(t):
    m = size_re.match(t)
    if not m:
        return 0
    return (int(m.group(1)) if m.group(1) else 1) * int(m.group(3))

def split_tail(c):
    t = tail_re.search(c)
    return (t.group(1), c[:t.start()].strip()) if t else ('', c)

files, unparsed, syms = [], [], Counter()

for path in sorted(glob.glob(os.path.join(FD_DIR, '*.*'))):
    recs, cur = [], None
    for n, raw in enumerate(open(path, encoding='latin-1'), 1):
        line = raw.rstrip('\r\n')
        if not line.strip():
            continue
        m = dir_re.match(line)
        if m:
            if m.group(2):
                syms[m.group(2).upper()] += 1
            continue
        m = hdr_re.match(line)
        if m:
            kind, nm, cm = m.group(1).upper(), m.group(2), (m.group(3) or '').strip()
            decl, cm = split_tail(cm) if cm else ('', '')
            overlay = (nm is None or nm.startswith(','))
            cur = {'kind': kind, 'name': None if overlay else nm,
                   'comment': cm, 'declared': decl, 'fields': []}
            recs.append(cur)
            continue
        m = fld_re.match(line)
        if m and cur is not None:
            nm, typ, val, cm = m.group(1), m.group(2), m.group(3), (m.group(4) or '').strip()
            prec, cm = split_tail(cm) if cm else ('', '')
            cur['fields'].append({'name': nm, 'type': typ, 'prec': prec,
                                  'val': val, 'comment': cm, 'w': width(typ)})
            continue
        if line.strip().startswith(';'):
            continue
        unparsed.append((os.path.basename(path), n, repr(line[:60])))
    files.append((path, recs))

mismatches = []
with open(OUT, 'w', encoding='utf-8') as o:
    o.write('# Record layouts\n\nGenerated from `SRC/FD/`.\n\n')
    tf = tr = tfl = 0
    for path, recs in files:
        if not recs:
            continue
        base = os.path.basename(path)
        tf += 1
        o.write('## %s\n\n' % base)
        for i, r in enumerate(recs):
            tr += 1
            tfl += len(r['fields'])
            calc = sum(f['w'] for f in r['fields'])
            title = r['name'] or '(overlay %d)' % i
            if r['declared']:
                d = width(r['declared'])
                bad = (d != calc)
                if bad:
                    mismatches.append((base, title, r['declared'], calc))
                note = ' - %s, declared %s, computed %d%s' % (
                    r['kind'], r['declared'], calc, '  **MISMATCH**' if bad else '')
            else:
                note = ' - %s, computed %d bytes' % (r['kind'], calc)
            o.write('### %s%s\n\n' % (title, note))
            if r['comment']:
                o.write('%s\n\n' % r['comment'])
            o.write('| Off | Field | Type | Prec | Init | Description |\n')
            o.write('|---|---|---|---|---|---|\n')
            off = 0
            for f in r['fields']:
                init = f['val'] if f['val'] else ''
                init = ''.join(c if 32 <= ord(c) < 127 else '.' for c in init)
                o.write('| %d | %s | %s | %s | %s | %s |\n' % (
                    off, f['name'] or '*(filler)*', f['type'],
                    f['prec'] or '', init, f['comment']))
                off += f['w']
            o.write('\n')
    o.write('---\n\n%d files, %d records, %d fields.\n' % (tf, tr, tfl))

print('files    :', len(files))
print('records  :', sum(len(r) for _, r in files))
print('fields   :', sum(len(x['fields']) for _, r in files for x in r))
print('unparsed :', len(unparsed))
print('directive symbols:', dict(syms))
print('mismatches:')
for m in mismatches:
    print('   %s  %s  declared %s vs computed %d' % m)
for u in unparsed[:20]:
    print('   %s:%s  %s' % u)
