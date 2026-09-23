# Running on Synergy/DE v12 (64-bit Windows)

This directory ports the system from DBL 4.41 for DOS to Synergy/DE v12
without a DOS emulator. The application source is unchanged apart from
57 lines of compile fixes, applied by `portfix.py` and described there.

**These scripts need the system's source tree, which is not published
here** (see the top-level README). They are the port as used against the
private archive: copy this directory into the root of the source tree as
`V12\` and run from there. `SECPROGS.TXT` and the key table in `NEWCO.DBL`
are derived from the source; everything else is new.

## Use

| Step | Command | When |
|---|---|---|
| Build | `V12\BUILD.BAT` | After any source change. Log in `V12\BUILD.LOG`. |
| Fresh test data | `V12\SETUP.BAT` (`/FRESH` to wipe) | Once. Makes TEST COMPANY (co. 1). |
| Run | `V12\ACCT.BAT` | Double-click. Sign on to company `01`. |

Requires Synergy/DE v12 (licensed) and Python 3 on `PATH`.

`WORK\` (runtime files) and `DAT\001-005\` (company data) are created by
`SETUP.BAT` and are outside git. `RUN\` stays as committed.

## What the port does

- **`ENV.BAT`** sets the `ACCSET.BAT` logicals relative to the checkout,
  leaving `DBLDIR` to Synergy.
- **`BUILD.BAT`** builds `XC.OLB`, then runs each `MAKxx.BAT` unchanged
  except for its hard-coded `SET FD=`.
- **`term.py`** is how the system is run. On a Windows desktop `dbr` draws
  in its own window, which does not interpret the VT100 sequences these
  programs write. With its terminal on pipes it writes them to stdout
  instead, so `term.py` runs `dbr` on pipes inside a normal console with
  VT processing on. It sends Enter as CR LF, as the DOS terminal did and
  as `INPTD`/`INPTA` expect, and clears the screen on 80/132-column
  switches as a VT100 does.
- **`TTSTS.DBL`** replaces the runtime's `TTSTS` in `XC.OLB`. On a pipe the
  built-in one always reports a key waiting, which hangs every report sent
  to `TT:` in `OPEN`'s terminal probe.
- **`SETUP.BAT`** copies `RUN\` to `WORK\`, then runs:
  - `NEWCO.DBL`: clears device-map lock counters, writes `COFILE.DDF` and
    `SECUR.ISM` (every secured program open to every company; list from
    `secprogs.py`), and creates the nine ISAM files from the key tables in
    `APOISM`, `AROISM` and `PAYISM`.
  - `newco_init.py`: runs the application's own `INITAP`, `INITAR`,
    `INITGL`, `INITBR` and `PRI10` with scripted answers (500 records per
    file) to create the relative files.
- **`drive.py`** runs a program with scripted keys and prints the screens;
  used by `newco_init.py` and for testing.

## Things to know

- Closing the window mid-program leaves files marked in use, as a crash
  did on DOS. Menu option **10, Clear File Protection**, fixes it.
- Terminal number is 0 under `dbr` on Windows; `NEWCO` maps it to
  company 1. Changing company goes through the sign-on as before.
- Printing to `LP:` has not been tried. Reports can go to the screen
  (`TT:`) or to a file.
