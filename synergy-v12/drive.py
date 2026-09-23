r"""Run a program under the Synergy runtime (dbr) with scripted keys.

    python V12/drive.py SY:IDCTRL "01\r" ...

Each argument after the program is a chunk of keyboard input (Python
escapes allowed, e.g. "\r", "\x1b"). The session runs in WORK\ with the
ENV.BAT environment; the 24x80 screens the program draws are rendered
and printed, one per screen clear, followed by the final screen and any
runtime messages. Used to smoke-test the port without a terminal.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROWS, COLS = 24, 80


class Screen:
    def __init__(self):
        self.shots = []
        self.clear()

    def clear(self):
        self.cells = [[' '] * COLS for _ in range(ROWS)]
        self.r = self.c = 0

    def text(self):
        lines = [''.join(row).rstrip() for row in self.cells]
        while lines and not lines[-1]:
            lines.pop()
        return '\n'.join(lines)

    def snap(self):
        t = self.text()
        if t.strip() and (not self.shots or self.shots[-1] != t):
            self.shots.append(t)

    def feed(self, data):
        i = 0
        while i < len(data):
            ch = data[i]
            if ch == '\x1b':
                m = re.match(r'\x1b\[([?\d;]*)([A-Za-z])|\x1b[78=>]', data[i:])
                if not m:
                    i += 1
                    continue
                args, cmd = m.group(1) or '', m.group(2)
                nums = [int(x) if x.isdigit() else 0 for x in args.split(';')] if args else []
                if cmd in 'Hf':
                    self.r = max((nums[0] if nums else 1) - 1, 0) % ROWS
                    self.c = max((nums[1] if len(nums) > 1 else 1) - 1, 0) % COLS
                elif cmd == 'J':
                    self.snap()
                    if (nums[:1] or [0])[0] == 2:
                        self.clear()
                    else:
                        for c in range(self.c, COLS):
                            self.cells[self.r][c] = ' '
                        for r in range(self.r + 1, ROWS):
                            self.cells[r] = [' '] * COLS
                elif cmd == 'K':
                    for c in range(self.c, COLS):
                        self.cells[self.r][c] = ' '
                elif cmd == 'C':
                    self.c = min(self.c + (nums[0] if nums else 1), COLS - 1)
                i += m.end()
                continue
            if ch == '\r':
                self.c = 0
            elif ch == '\n':
                self.r = min(self.r + 1, ROWS - 1)
            elif ch == '\b':
                self.c = max(self.c - 1, 0)
            elif ch >= ' ':
                self.cells[self.r][self.c] = ch
                self.c = min(self.c + 1, COLS - 1)
            i += 1


def run(program, keys, timeout=20):
    """Output so far, plus a note if the program was still running at timeout."""
    import tempfile
    cmd = f'call "{ROOT}\\V12\\ENV.BAT" && cd /d "{ROOT}\\WORK" && dbr {program}'
    with tempfile.TemporaryFile() as out:
        p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,
                             stdout=out, stderr=subprocess.STDOUT)
        p.stdin.write(keys.encode('latin-1'))
        p.stdin.close()
        try:
            p.wait(timeout)
            note = ''
        except subprocess.TimeoutExpired:
            subprocess.run(['taskkill', '/F', '/T', '/PID', str(p.pid)],
                           capture_output=True)
            p.wait()
            note = f'%DBR- [drive.py: still waiting for input after {timeout}s; killed]'
        out.seek(0)
        return out.read().decode('latin-1') + note


if __name__ == '__main__':
    keys = ''.join(a.encode('latin-1').decode('unicode_escape') for a in sys.argv[2:])
    out = run(sys.argv[1], keys)
    tail = re.split(r'(?=%DBR-)', out, maxsplit=1)
    s = Screen()
    s.feed(tail[0])
    s.snap()
    for n, shot in enumerate(s.shots, 1):
        print(f'----- screen {n} ' + '-' * 60)
        print(shot)
    if len(tail) > 1:
        print('----- runtime ' + '-' * 60)
        print(tail[1].strip())
