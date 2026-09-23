"""List every program name the menus pass to XCALL SECUR.

Writes V12/SECPROGS.TXT, one name per line, which NEWCO reads to build a
security file granting every program to every company. Run from the
checkout root.
"""
import re
from pathlib import Path

names = set()
for p in sorted(Path('SRC').glob('*/*.DBL')):
    text = p.read_bytes().decode('latin-1').replace('\r', '')
    for m in re.finditer(r"XCALL\s+SECUR\s*\(\s*\d+\s*,\s*(\w+|'[^']*')", text, re.I):
        arg = m.group(1)
        if arg.startswith("'"):
            names.add(arg.strip("'").strip().upper())
            continue
        # the table declaration and its & continuation lines
        decl = re.search(r'^\s*' + arg + r'\s*,.*(?:\n&.*)*', text, re.I | re.M)
        names.update(s.strip().upper() for s in re.findall(r"'([^']*)'", decl.group(0)))
names.discard('')
Path('V12/SECPROGS.TXT').write_text(''.join(n + '\n' for n in sorted(names)))
print(len(names), 'programs')
