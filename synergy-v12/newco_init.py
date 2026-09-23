r"""Create company 1's relative files by running the application's own
INIT programs with scripted answers, as an installer would have at the
keyboard. Run by SETUP.BAT after NEWCO; every file is sized for 500
records. Stops with an error if any step leaves a file protected in
DEVICE.001 or a program fails.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from drive import ROOT, run

E = '\r\n'                     # Enter: CR, then the LF INPTD/INPTA discard
N = '500' + E                  # max records per file
Y = 'Y' + E

STEPS = [
    # A/P: nine files, no changes, interface to G/L; chains to SETDTL
    # (interface with detail), then SETVCH (vouchers start at 1)
    ('AP:INITAP', N * 9 + E + Y + E + Y + '1' + E),
    # A/R: six sized files, header + letter files, category file; chains
    # to BLDCAT (five salesmen on sales commission), then AROISM (nothing)
    ('AR:INITAR', N * 6 + Y + Y + N + E
                  + '5' + E + ''.join(f'{i}{E}S{E}' for i in range(1, 6))
                  + ('N' + E) * 5 + E + 'N' + E),
    # G/L: four sized files, no profit centres, interface file; no schedules
    ('GL:INITGL', N * 4 + 'N' + E + N + E + 'N' + E),
    # Bank reconciliation
    ('BR:INITBR', N + E + Y),
    # Payroll: all parameter files, blank company status, sized logs
    ('PAY:PRI10', Y * 4 + E + N * 2 + Y * 2 + N * 3 + Y * 5 + E + Y),
]


def locks():
    lines = (ROOT / 'WORK' / 'DEVICE.001').read_text('latin-1').splitlines()[1:]
    return [l[:4] for l in lines if l[4:8] != '0000']


for program, keys in STEPS:
    out = run(program, keys, timeout=30)
    failed = 'drive.py: still waiting' in out or '-E-' in out or '-F-' in out
    held = locks()
    print(f'{program:10} {"FAILED" if failed or held else "ok"}'
          + (f'  locked: {held}' if held else ''))
    if failed or held:
        print(out[-1500:])
        sys.exit(1)
