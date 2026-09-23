r"""Run the accounting system in an ordinary Windows console window.

    python V12\term.py [PROGRAM]        (default SY:IDCTRL, the sign-on)

On a Windows desktop, dbr draws in its own Synergy window, which does not
interpret the ANSI/VT100 sequences these programs write, so the screens
come out as escape-code litter. With its input and output on pipes, dbr
instead reads keystrokes from stdin and writes the raw sequences to
stdout. This bridge sits in between: it switches the console to VT
processing, passes dbr's output straight through, and passes keys in,
translated the way the DOS terminal sent them:

    Enter           CR LF   (INPTD/INPTA read and discard the LF)
    F1-F10, arrows  NUL + scan code, as DBL for DOS delivered them
                    (F9 = abort, F10 = back up a field, as on DOS)
"""
import ctypes
import msvcrt
import os
import subprocess
import sys
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
k32 = ctypes.windll.kernel32

VT_PROCESSING = 0x0004          # ENABLE_VIRTUAL_TERMINAL_PROCESSING
NO_AUTO_RETURN = 0x0008         # DISABLE_NEWLINE_AUTO_RETURN: LF is LF, as on a VT100


def console_vt():
    out = k32.GetStdHandle(-11)
    mode = ctypes.c_uint()
    if not k32.GetConsoleMode(out, ctypes.byref(mode)):
        sys.exit('term.py must run in a console window.')
    if not k32.SetConsoleMode(out, mode.value | VT_PROCESSING | NO_AUTO_RETURN):
        sys.exit('This console cannot display ANSI screens (needs Windows 10 or later).')


def pump_output(src):
    """dbr's output to the screen, as it arrives.

    Reports switch the VT100 to 132 columns and back (ESC[?3h / ESC[?3l,
    in BEGTT and ENDTT). A real VT100 clears the screen when it does, and
    the programs rely on that; Windows consoles don't, so it's added here.
    """
    while True:
        chunk = src.read(4096)
        if not chunk:
            return
        text = chunk.decode('cp437')
        for mode in ('\x1b[?3h', '\x1b[?3l'):
            text = text.replace(mode, mode + '\x1b[H\x1b[2J')
        sys.stdout.write(text)
        sys.stdout.flush()


def main():
    program = sys.argv[1] if len(sys.argv) > 1 else 'SY:IDCTRL'
    work = ROOT / 'WORK'
    if not (work / 'COFILE.DDF').exists():
        sys.exit(r'No installation in WORK\. Run V12\SETUP.BAT first.')
    console_vt()
    k32.SetConsoleTitleW('Accounting')

    dbr = subprocess.Popen(['dbr', program], cwd=work, stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                           bufsize=0)
    reader = threading.Thread(target=pump_output, args=(dbr.stdout,), daemon=True)
    reader.start()

    def send(b):
        try:
            dbr.stdin.write(b)
            dbr.stdin.flush()
        except OSError:
            pass

    while dbr.poll() is None:
        try:
            if not msvcrt.kbhit():
                reader.join(0.01)
                continue
            ch = msvcrt.getwch()
        except KeyboardInterrupt:
            ch = '\x03'
        if ch == '\r':
            send(b'\r\n')
        elif ch in ('\x00', '\xe0'):                    # function / cursor key
            send(b'\x00' + bytes([ord(msvcrt.getwch()) & 0xFF]))
        else:
            send(ch.encode('cp437', 'replace'))
    reader.join(1)


if __name__ == '__main__':
    main()
