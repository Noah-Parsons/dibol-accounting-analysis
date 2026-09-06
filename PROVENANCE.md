# Provenance

This system was described to me as having been assembled from several
separate programs. This file records what the source says about its
own origins, and what remains unknown.

The short answer, on the evidence below: it appears to be a
**configurable commercial accounting package**, sold with optional
modules, whose payroll and ledger halves were written by different
groups of people beginning in 1980.

## Method

Derived from comment headers, conditional-compilation symbols, call
sites and build scripts across `SRC/`, plus a rebuild of the shared
library from a clean clone.

Limitations, stated plainly:

- Authorship coverage is partial: 245 of 776 `.DBL` files carry a
  `WRITTEN BY` header, about 32%.
- Headers are self-reported comments, not verified metadata. Most
  `MODIFIED BY` lines are empty template stubs never filled in.
- All file timestamps reflect the 2026 copy date and carry no
  historical information.
- Two header conventions coexist: `WRITTEN BY: XXX (MMM YY)` with
  initials, and `WRITTEN BY FULL NAME` without a date. Some authors
  appear under both.

## Three distinct author populations

Authorship splits along subsystem lines into three groups with minimal
overlap:

| Group | Subsystems | Authors |
|---|---|---|
| A | `PR/` payroll, `XC/` shared library, `SC/` security, `BR/` bank rec | WBK, CJS, LWB (Loren Bergeson), JLS |
| B | `AP/`, `AR/`, `SY/` | David Hawkinson, Dan Roesler |
| C | `GL/` general ledger | Deb Haffner, DER |

Counts by subsystem:

- `PR/` — WBK (~44), CJS (~35), LWB (~28), JLS (8), Dan Roesler (6),
  Darin Capp (3), Jackie Soule (1)
- `XC/` — Loren Bergeson (32), CJS (13), LWB (3), WBK (1)
- `SC/` — CJS (13), WBK (2)
- `BR/` — WBK (5)
- `AR/` — David Hawkinson (8), Dan Roesler (8), WBK (2), RAN (1)
- `AP/` — David Hawkinson (8), Dan Roesler (2)
- `GL/` — Deb Haffner (3), DER (1)
- `SY/` — Dan Roesler (1)
- `FD/` — none; these are record definitions rather than programs

Group A is dense and multi-authored, and includes the shared
subroutine library the whole system links against. Group B wrote the
ledger modules against that library. Group C wrote the general ledger
and appears nowhere else in 990 files.

Overlap is limited to Dan Roesler (6 files in `PR/`) and WBK (2 files
in `AR/`).

## Identified people

Full names recovered from the no-date header format:

- **Loren Bergeson** — LWB. Principal author of `XC/`, major
  contributor to `PR/`.
- **David Hawkinson** — `AP/` and `AR/`. Appears under no initials.
- **Dan Roesler** — `AP/`, `AR/`, `SY/`, and part of `PR/`. The only
  author spanning groups A and B.
- **Deb Haffner** — DEB. Sole named author of `GL/`.
- **Darin Capp** — DARIN. `PR/`.
- **Jackie Soule** — `PR/`.

Unresolved initials: **CJS**, **WBK**, **JLS**, **RAN**, **DER**, and —
appearing only as modifiers — **TLW**, **PCB**, **MRC**.

WBK modified far more files than he wrote, indicating a long-term
maintenance role.

## Dates

Of parseable dates: 1980 (83), 1983 (12), 1981 (3), 1982 (3), 1985 (2),
1986 (2), 1984 (1).

A 1980 core, actively maintained for roughly six years, then
substantially frozen.

## A configurable commercial product

604 of roughly 990 source files — **60%** — carry `.IFDEF`
conditionals. The symbols fall into two classes.

**Platforms:** UNIX (1946), RT11 (1692), VAX (1225), RSTS (8),
MSDOS (1).

**Feature flags:** JCST (150), ECST (95), UCST (92), BATCH (76),
BNKREC (60), BANK (50), SCTRM (33), SCCMP (32), CERT (8), COMLOG (6),
DS (5), TEST (2), VT100 (1), FANSI (1).

The feature flags compile optional modules in or out — cost-accounting
variants, bank reconciliation, batch processing, certification,
terminal-versus-compiled screen handling. A single source tree that
builds several different product configurations is the signature of a
package sold to system integrators, which was precisely DBL's target
market.

This makes "purchased as a product, with modules selected at
purchase" the likeliest answer to the origin question, and reframes
"assembled from several programs" as a description of a configurable
suite rather than of ad-hoc stitching.

## Platform history

The source records five platforms:

| Platform | Evidence |
|---|---|
| DEC PDP-11 under RT-11 | `.IFDEF RT11` (1692); `FD:` logical-device includes |
| Unix | `.IFDEF UNIX` (1946); `SRC/SY/MAKDES` is a shell script; nine files retain LF endings |
| DEC VAX | `.IFDEF VAX` (1225), concentrated in date handling (`DFDATA.FD`) |
| DEC RSTS | `.IFDEF RSTS` (8) |
| Novell NetWare | `DBLPQUE.NOV` in the runtime — print queue support |
| MS-DOS | `.BAT` build scripts; DBL 4.41 for DOS |

Unix, RT-11 and VAX are near-equal, indicating three targets
maintained in parallel rather than a succession of migrations.
`MSDOS` appears exactly once, which means the DOS port made DOS the
unmarked default rather than adding branches — the build was ported,
not the source. `SRC/SY/MAKDES` survives in both a Unix shell version
and a `.BAT` version, consistent with that.

`SRC/BR/CVTP35.DBL` widens a date field to four digits — Y2K
remediation, undated but necessarily from the 1990s.

## Language and toolchain

Built with **DBL 4.41 for DOS**, released October 1991
(`DBL/RELEASE.TXT`).

DBL is a DIBOL-compatible language developed by Digital Information
Systems Corporation (DISC), renamed Synergex in 1996, and sold today
as part of Synergy/DE. DBL reached the PDP-11 under RT-11 in 1980 —
the same year as the oldest headers here, so this application was
written essentially as soon as the platform existed.

The compiler and runtime in `DBL/` are a commercial third-party
product and are excluded from this repository.

## Verified reproducible build

The shared library was rebuilt from a fresh clone of this repository
using DBL 4.41 under FreeDOS 1.4, and compared byte-for-byte against
the library that had been running in production.

- 1,246 differing bytes out of 184,723 (0.67%)
- Differences occur in nine-byte clusters at object-library member
  header offsets
- Every differing byte in the entire file is one of twelve
  characters: `A`, `J`, `g`, `l`, `0`, `1`, `2`, `3`, `4`, `5`, `7`,
  `9` — the letters spelling "Aug" and "Jul", and date digits

The two libraries are identical apart from embedded build timestamps.
1980 source, compiled with a 1991 toolchain, in 2026, produces the
same artefact.

The application then ran, reaching its own file-open error handler
because the excluded data files are absent — the expected stopping
point.

## Completeness

Comparing 769 source names against the 519 `.DBR` runnables in the
production tree: **zero runnables lack source**. Every program in
production has its source here.

The 250 source files without a runnable are the 76 `XC/` library
modules, which compile into `XC.OLB` rather than standalone, plus
feature-flagged modules never built for this configuration. This
repository therefore holds more of the product than the deployment
used.

`EXC/` in the production tree contains only `AP AR BR GL PR SC SY`.
The `JA`, `JC`, `OE` and `FRM` paths in `ACCSET.BAT` are vestigial —
modules never installed.

## Shared library usage

14,503 `XCALL` sites across the source, about 15 per file. The most
called routines are all screen handling and protected file access:
ABRTP (1394), CLRSC (1323), OPENP (1292), INPTD (1133), CLOSP (906),
WRITS (804), READ (775), INPTA (682), INUSE (631). Every program
follows the same skeleton, which is why a codebase written by a dozen
people across four platforms remains coherent.

Roughly 22 of the 76 library modules are never called and are dead
weight compiled into every build, including the date-arithmetic
family (DDAY, DDIF, DOW), both check-digit routines, and FILE3
through FILE9. Date arithmetic going unused in accounting software
suggests it was called on a platform this build no longer targets.

`XCALL` also serves program-to-program calls, so the call graph has a
second layer beyond the library.

## Scale

161,973 lines of DBL.

| Subsystem | Files | Lines |
|---|---|---|
| PR | 202 | 47,796 |
| AR | 184 | 37,043 |
| AP | 134 | 30,808 |
| GL | 120 | 30,437 |
| XC | 76 | 7,213 |
| SY | 34 | 4,347 |
| SC | 15 | 2,989 |
| BR | 10 | 1,340 |

Comment density 3.2%. Programs range from 11 to 960 lines; the
largest is `W2S.DBL`, which produces W-2s.

## Data structures

See `SCHEMA.md` — 339 records and 2,425 fields extracted from
`SRC/FD/` by `tools-fdparse.py`, with computed byte offsets.

Notable:

- `.FDC` files declare `COMMON` blocks; `.FD` files declare `RECORD`.
- `RECORD ,X` marks an overlay redefinition of the same buffer.
- Field types support repeat counts (`,18D7`) and literal initial
  values (`,A2 ,'00'`).
- The right-hand comment column carries implied decimal places the
  declaration omits — `,D7` annotated `D7.4`. This is a migration
  hazard: the declaration alone loses the decimal point.
- `SRC/FD/SCREEN.FDC` builds ANSI cursor-positioning sequences as a
  record, with row and column as writable fields.
- `PAYCRD.FD` is an 80-column punched-card image whose overlays each
  begin with a card-code field — an input format that survived every
  platform migration unchanged.
- Social Security numbers are stored as nine unformatted digits
  (`NSOCS ,D9`).

## Copyright status: UNRESOLVED

A search of all 990 files for `COPYRIGHT`, `(C)` and `ALL RIGHTS`
returned no matches. No company name, vendor attribution or rights
statement appears anywhere in the source.

**The absence of a notice does not establish that the code is
unencumbered.** This is an open question and nothing here should be
read as a legal conclusion. Note that the feature-flag evidence above
makes third-party commercial origin more likely, not less.

## Note on `AUTOEXEC.BAT`

`AUTOEXEC.BAT` in this repository is Microsoft's stock NTVDM
template, not part of the application. It appears to have been swept
into the tree during the Windows XP deployment.

## Open questions

Put to the original operator 24 August 2026; answers pending.

1. Was this bought as a product, with modules chosen at purchase? The
   feature flags suggest so — which vendor, and when?
2. Where did the group A code (payroll, shared library, security,
   bank rec) come from?
3. Where did group B (`AP/`, `AR/`, `SY/`) come from, and was it
   written deliberately against the group A library?
4. `GL/` is Deb Haffner's alone. Who was she, and where did the
   general ledger come from?
5. Who are CJS, WBK, JLS, RAN and DER? Employees, contractors, or a
   vendor's staff?
6. Do any purchase agreements, licences, invoices or correspondence
   survive?
7. Was there ever a support contract, and with whom?
8. Where was DBL 4.41 purchased, and does a licence or serial exist?
9. Was the system originally run on a PDP-11, and later on a VAX or a
   NetWare network?
