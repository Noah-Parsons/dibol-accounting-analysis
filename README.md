# Analysis of a Legacy DBL Accounting System (1980-2026)

Documentation and analysis tooling produced during the preservation of a
multi-module accounting system written in DBL, in continuous production use
from 1980 until 2026.

The system was developed by Custom Computer Services, a company that no longer
exists. It comprises 161,973 lines across 519 programs and eight subsystems,
and ran on at least six platforms over its life: DEC RT-11, RSTS/E, VAX, Unix,
Novell NetWare and MS-DOS.

**The system's own source code is not published here.** Its copyright belongs
to the developer's successors in interest, which have not been identified.
The archive is held privately pending resolution of that question. Any rights
holder is invited to make contact.

## Contents

| File | Description |
|---|---|
| `dibol-report-v2.pdf` | Technical report: preservation method, verification, and analysis |
| `SCHEMA.md` | 339 record layouts and 2,425 fields with computed byte offsets, extracted from the system's field definitions |
| `XREF.csv` | 2,567 program-to-record dependency pairs |
| `PROVENANCE.md` | Authorship analysis derived from source comment headers |
| `tools-fdparse.py` | The parser that generates `SCHEMA.md` |

## Summary of findings

- Every program in production has surviving source, verified by comparing 519
  compiled programs against 769 source files
- The shared library, rebuilt from archived source using the original 1991
  compiler, is byte-identical to the library running in production apart from
  embedded build timestamps
- 604 of 990 source files carry conditional compilation, with UNIX, RT-11 and
  VAX maintained in parallel rather than in succession
- A second class of conditionals compiles optional modules in and out,
  indicating a configurable product rather than bespoke software
- 742 of 775 source files compile without modification under Synergy/DE
  version 12, thirty-five years after the toolchain they were written for

## Licence

Documentation, including the report, schema, dependency map and provenance
record, is licensed CC BY 4.0.

`tools-fdparse.py` is licensed MIT.

## Citation

See the Zenodo record for the DOI and citation details.
