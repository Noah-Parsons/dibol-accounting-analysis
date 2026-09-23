"""One-time source fixes for Synergy/DE v12.

Each fix rewrites a construct DBL 4.41 accepted and Synergy v12 rejects,
without changing what the program does. Run from the checkout root;
it prints every line it changes. Line endings are preserved.
"""
import re
import sys
from pathlib import Path

SRC = Path('SRC')

# PROC (n) -> PROC: v12 rejects the channel count; it only reserved
# PDP-11 I/O buffers, and Synergy allocates channels on demand.
PROC_FILES = ['AP/APAJVM', 'AP/INITAP', 'AP/UPVMAS', 'AR/AROCTL', 'AR/CLRSLS',
              'AR/CLRMOS', 'AR/CLRCSH', 'AR/CLRMOC', 'GL/INITCN', 'GL/INITGL',
              'PR/PC155']

# Misplaced dots in relational operators: "X .LT .16", "10. OR.", "I. EQ. 0".
OPS = r'(EQ|NE|LT|GT|LE|GE|AND|OR)'
DOT_FILES = ['SY/INMENU', 'AR/INMENU', 'AR/ARMENU', 'AP/NAP5', 'AR/STMENT',
             'PR/PX108', 'PR/PB108']

# Formatted assignment from an alpha field holding digits: DBL 4 converted
# implicitly, v12 needs an explicit ^D().
ALPHA_FMT = {
    'SY/CFMANT': ['FID'], 'SY/PRTCOF': ['CFFID'], 'AP/TEN99I': ['CFFID'],
    'AP/TEN99M': ['CFFID'], 'PR/PD170': [r'PT120\(\d\)'],
    'PR/PE220': [r'PT120\(\d\)'],
}

# Trailing-minus initial value: ,000001-  ->  ,-000001
MINUS_FILES = ['AR/CSHEDT', 'AR/CSHJNL', 'AR/CSHDSP']

# IF ... THEN BEGIN ... END with no ELSE: v12 requires ELSE after THEN.
THEN_FILES = ['AR/STMENT', 'PR/PF450', 'PR/PJ100']


def code(line):
    """Line with comment and string literals blanked, for keyword scanning."""
    out, q = [], None
    for ch in line:
        if q:
            out.append(' ')
            if ch == q:
                q = None
        elif ch in "'\"":
            q = ch
            out.append(' ')
        elif ch == ';':
            break
        else:
            out.append(ch)
    return ''.join(out).upper()


def drop_orphan_then(lines):
    changed = []
    words = [re.findall(r'\b(THEN|BEGIN|END|ELSE)\b', code(l)) for l in lines]
    for i, ws in enumerate(words):
        if 'THEN' not in ws:
            continue
        # only THEN BEGIN blocks; a one-statement THEN is followed by its ELSE
        after = ws[ws.index('THEN') + 1:] or (words[i + 1] if i + 1 < len(words) else [])
        if not after or after[0] != 'BEGIN':
            continue
        # walk forward from THEN to the matching END of its BEGIN block
        depth, j, k, started = 0, i, ws.index('THEN') + 1, False
        end_at = None
        while j < len(lines) and end_at is None:
            for n, w in enumerate(words[j][k:], k):
                if w == 'BEGIN':
                    depth += 1
                    started = True
                elif w == 'END' and started:
                    depth -= 1
                    if depth == 0:
                        end_at = (j, n)
                        break
            j, k = j + 1, 0
        if end_at is None:
            continue
        ej, en = end_at
        rest = words[ej][en + 1:]
        nxt = rest[0] if rest else next(
            (code(l).split()[0] for l in lines[ej + 1:] if code(l).strip()), '')
        if nxt != 'ELSE':
            lines[i] = re.sub(r'\bTHEN\b ?', '', lines[i], count=1, flags=re.I)
            changed.append(i)
    return changed


def edit(rel, fn):
    p = SRC / (rel + '.DBL')
    raw = p.read_bytes().decode('latin-1')
    lines = raw.splitlines(keepends=True)
    before = list(lines)
    fn(lines)
    for n, (a, b) in enumerate(zip(before, lines), 1):
        if a != b:
            print(f'{rel}:{n}\n  - {a.rstrip()}\n  + {b.rstrip()}')
    p.write_bytes(''.join(lines).encode('latin-1'))


def sub_all(pattern, repl):
    def fn(lines):
        for i, l in enumerate(lines):
            lines[i] = re.sub(pattern, repl, l, flags=re.I)
    return fn


for f in PROC_FILES:
    edit(f, sub_all(r'^PROC \(\d+\)', 'PROC'))
for f in DOT_FILES:
    def fn(lines):
        for i, l in enumerate(lines):
            l = re.sub(r'\.' + OPS + r' \.(\d)', r'.\1. \2', l)        # .LT .16
            l = re.sub(r'(\w)\. ' + OPS + r'\. ', r'\1 .\2. ', l)       # 10. OR.  I. EQ.
            lines[i] = l
    edit(f, fn)
for f, fields in ALPHA_FMT.items():
    for fld in fields:
        edit(f, sub_all(r'= ?(' + fld + r') ?,', r'= ^D(\1),'))
for f in MINUS_FILES:
    edit(f, sub_all(r',(\d+)-(\s*)$', r',-\1\2'))
for f in THEN_FILES:
    edit(f, drop_orphan_then)
