# Record layouts

Generated from `SRC/FD/`.

## ADJMS.FD

### ADJMS - RECORD, declared A33, computed 33

ADJUSTMENTTRX MASTER RECORD (ADJMS.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | AJDES | A25 |  |  | DESCRIPTION |
| 25 | AJTYP | A1 |  |  | TYPE |
| 26 | AJGL | D7 |  |  | G/L NUMBER |

## ADRMS.FDC

### ADRMS - COMMON, declared A31, computed 31

CITY STATE ZIP MASTER FILE (ADRMS.FDC)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | ADR01 | A5 |  |  | ID NUMBER |
| 5 | ADR05 | A15 |  |  | CITY |
| 20 | ADR10 | A2 |  |  | STATE |
| 22 | ADR15 | A9 |  |  | ZIP |

## APADJ.FD

### APADJ - RECORD, declared A398, computed 398

A/P ADJUSTMENT FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | AJVND | D4 | D4 |  | VENDOR NUMBER |
| 4 | AJVCH | D6 | D6 |  | VOUCHER NUMBER |
| 10 | AJINO | A35 | A35 |  | INVOICE NUMBER |
| 45 | AJIDT | D8 | D8 |  | INVOICE DATE |
| 53 | AJDDT | D8 | D8 |  | DUE DATE |
| 61 | AJPCT | D3 | D3.1 |  | DISCOUNT PERCENT |
| 64 | AJDSC | D8 | D8.2 |  | DISCOUNT AMOUNT |
| 72 | AJAMT | D10 | D10.2 |  | ORIGINAL INVOICE AMOUNT |
| 82 | AJADJ | D10 | D10.2 |  | ADJUSTMENT AMOUNT |
| 92 | AJACT | 18D7 | A126 |  | G/L ACCOUNT NUMBERS |
| 218 | AJDST | 18D10 | A180 |  | G/L DISTRIBUTION |

### AJCTL - RECORD, computed 398 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A16 |  |  |  |
| 16 | AJINT | D1 |  |  |  |
| 17 | *(filler)* | A363 |  |  |  |
| 380 | AJORG | D5 |  |  | ORGANIZED COUNT |
| 385 | AJREC | D5 |  |  | RECORD COUNT |
| 390 | AJMAX | D5 |  |  | MAXIMUM # OF RECORDS |
| 395 | AJDEL | D3 |  |  | DELETE COUNT |

## APADJ.FDC

### APADJ - COMMON, declared A398, computed 398

A/P ADJUSTMENT FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | AJVND | D4 | D4 |  | VENDOR NUMBER |
| 4 | AJVCH | D6 | D6 |  | VOUCHER NUMBER |
| 10 | AJINO | A35 | A35 |  | INVOICE NUMBER |
| 45 | AJIDT | D8 | D8 |  | INVOICE DATE |
| 53 | AJDDT | D8 | D8 |  | DUE DATE |
| 61 | AJPCT | D3 | D3.1 |  | DISCOUNT PERCENT |
| 64 | AJDSC | D8 | D8.2 |  | DISCOUNT AMOUNT |
| 72 | AJAMT | D10 | D10.2 |  | ORIGINAL INVOICE AMOUNT |
| 82 | AJADJ | D10 | D10.2 |  | ADJUSTMENT AMOUNT |
| 92 | AJACT | 18D7 | A126 |  | G/L ACCOUNT NUMBERS |
| 218 | AJDST | 18D10 | A180 |  | G/L DISTRIBUTION |

### AJCTL - COMMON, computed 398 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A16 |  |  |  |
| 16 | AJINT | D1 |  |  |  |
| 17 | *(filler)* | A363 |  |  |  |
| 380 | AJORG | D5 |  |  | ORGANIZED COUNT |
| 385 | AJREC | D5 |  |  | RECORD COUNT |
| 390 | AJMAX | D5 |  |  | MAXIMUM # OF RECORDS |
| 395 | AJDEL | D3 |  |  | DELETE COUNT |

## APGL.FD

### APGL1 - RECORD, declared A20, computed 20

RECORD #1 A/P TO G/L

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A10 |  |  |  |
| 10 | APPPD | D10 | D10.2 |  | PREPAID CHECK AMOUNT |

### APGL2 - RECORD, computed 20 bytes

RECORD #2 A/P TO G/L

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | APPDS | D10 | D10.2 |  | PREPAID DISCOUNTS TAKEN |
| 10 | APCHK | D10 | D10.2 |  | REGULAR CHECK AMOUNTS |

### APGL3 - RECORD, computed 20 bytes

RECORD #3 A/P TO G/L

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | APRDS | D10 | D10.2 |  | REGULAR DISCOUNTS TAKEN |
| 10 | APAPO | D10 | D10.2 |  | NEW A/P OPEN ADDED AMOUNT |

### APGL - RECORD, computed 20 bytes

RECORDS #4 TO MAX #

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | APAMT | D10 | D10.2 |  | G/L EXPENSE AMOUNT |
| 10 | APACT | D7 | D7 |  | G/L ACCOUNT # |
| 17 | *(filler)* | A3 |  |  |  |

## APOPN.FD

### APOPN - RECORD, declared A116, computed 116

A/P OPEN FILE (APOPN.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | POVND | D4 | D4 |  | VENDOR NUMBER |
| 4 | POVCH | D6 | D6 |  | VOUCHER NUMBER |
| 10 | POINO | A35 | A35 |  | INVOICE NUMBER |
| 45 | POIDT | D8 | D8 |  | INVOICE DATE |
| 53 | POAMT | D10 | D10.2 |  | INVOICE AMOUNT |
| 63 | PODSC | D8 | D8.2 |  | DISCOUNT AMOUNT |
| 71 | PODDT | D8 | D8 |  | DUE DATE |
| 79 | POSTF | D1 | D1 |  | STATUS FLAG |
| 80 | POCHK | D6 | D6 |  | CHECK NUMBER |
| 86 | POJOB | D4 | D4 |  | JOB COST NUMBER |
| 90 | POPDD | D8 | D8 |  | PRE-PAID PARTIAL DUE DATE |
| 98 | POPAM | D10 | D10.2 |  | PRE-PAID PARTIAL AMOUNT |
| 108 | POPDS | D8 | D8.2 |  | PRE-PAID PARTIAL DISCOUNT |

### (overlay 1) - RECORD, computed 4 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | POVNA | A4 |  |  | ALPHA VENDOR NUMBER |

### POCTL - RECORD, computed 116 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A7 |  |  |  |
| 7 | POCUT | D8 |  |  | CUT OFF DATE |
| 15 | POFFG | D1 |  |  | (UNUSED) |
| 16 | *(filler)* | A82 |  |  | G/L INTERFACE FLAG IS IN POSITION 17 |
| 98 | POORG | D5 |  |  | ORGANIZE COUNT |
| 103 | POREC | D5 |  |  | RECORD COUNT |
| 108 | POMAX | D5 |  |  | MAXIMUM COUNT |
| 113 | PODEL | D3 |  |  | DELETE COUNT |

### (overlay 3) - RECORD, computed 90 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | POVN2 | D4 |  |  |  |
| 4 | POVC2 | D6 |  |  |  |
| 10 | *(filler)* | A62 |  |  |  |
| 72 | POCDT | D8 |  |  |  |
| 80 | POCNO | D6 |  |  |  |
| 86 | POBVN | D4 |  |  |  |

## APOPN.FDC

### APOPN - COMMON, declared A116, computed 116

A/P OPEN FILE (APOPN.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | POVND | D4 | D4 |  | VENDOR NUMBER |
| 4 | POVCH | D6 | D6 |  | VOUCHER NUMBER |
| 10 | POINO | A35 | A35 |  | INVOICE NUMBER |
| 45 | POIDT | D8 | D8 |  | INVOICE DATE |
| 53 | POAMT | D10 | D10.2 |  | INVOICE AMOUNT |
| 63 | PODSC | D8 | D8.2 |  | DISCOUNT AMOUNT |
| 71 | PODDT | D8 | D8 |  | DUE DATE |
| 79 | POSTF | D1 | D1 |  | STATUS FLAG |
| 80 | POCHK | D6 | D6 |  | CHECK NUMBER |
| 86 | POJOB | D4 | D4 |  | JOB COST NUMBER |
| 90 | POPDD | D8 | D8 |  | PRE-PAID PARTIAL DUE DATE |
| 98 | POPAM | D10 | D10.2 |  | PRE-PAID PARTIAL AMOUNT |
| 108 | POPDS | D8 | D8.2 |  | PRE-PAID PARTIAL DISCOUNT |

### (overlay 1) - COMMON, computed 4 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | POVNA | A4 |  |  | ALPHA VENDOR NUMBER |

### POCTL - COMMON, computed 116 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A7 |  |  |  |
| 7 | POCUT | D8 |  |  | CUT OFF DATE |
| 15 | POFFG | D1 |  |  | (UNUSED) |
| 16 | *(filler)* | A82 |  |  | G/L INTERFACE FLAG IS IN POSITION 17 |
| 98 | POORG | D5 |  |  | ORGANIZE COUNT |
| 103 | POREC | D5 |  |  | RECORD COUNT |
| 108 | POMAX | D5 |  |  | MAXIMUM COUNT |
| 113 | PODEL | D3 |  |  | DELETE COUNT |

### (overlay 3) - COMMON, computed 90 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | POVN2 | D4 |  |  |  |
| 4 | POVC2 | D6 |  |  |  |
| 10 | *(filler)* | A62 |  |  |  |
| 72 | POCDT | D8 |  |  |  |
| 80 | POCNO | D6 |  |  |  |
| 86 | POBVN | D4 |  |  |  |

## APT1F.FD

### APT1F - RECORD, declared A116, computed 116

TEMPORARY A/P OPEN FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | A1VND | D4 | D4 |  | VENDOR NUMBER |
| 4 | A1VCH | D6 | D6 |  | VOUCHER NUMBER |
| 10 | A1INO | A35 | A35 |  | INVOICE NUMBER |
| 45 | A1IDT | D8 | D8 |  | INVOICE DATE |
| 53 | A1AMT | D10 | D10 |  | INVOICE AMOUNT |
| 63 | A1DSC | D8 | D8 |  | DISCOUNT AMOUNT |
| 71 | A1DDT | D8 | D8 |  | DUE DATE |
| 79 | A1STF | D1 | D1 |  | STATUS FLAG |
| 80 | A1CHK | D6 | D6 |  | CHECK NUMBER |
| 86 | A1JOB | D4 | D4 |  | JOB COST NUMBER |
| 90 | *(filler)* | A26 | A26 |  | NOT USED |

## APT2F.FD

### APT2F - RECORD, declared A101, computed 101

TEMPORARY FILE OF CHECKS PRINTED

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | A2VND | D4 | D4 |  | VENDOR NUMBER |
| 4 | A2NAM | A25 | A25 |  | VENDOR NAME |
| 29 | A2INO | A35 | A35 |  | INVOICE NUMBER |
| 64 | A2IDT | D8 | D8 |  | INVOICE DATE |
| 72 | A2AMT | D10 | D10.2 |  | CHECK AMOUNT |
| 82 | A2DPD | D8 | D8 |  | DATE PAID |
| 90 | A2CHK | D6 | D6 |  | CHECK NUMBER |
| 96 | A2JOB | D4 | D4 |  | JOB NUMBER |
| 100 | A2FLG | D1 | D1 |  | CLEAR FLAG |

### A2CTL - RECORD, computed 101 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A96 |  |  |  |
| 96 | A2REC | D5 |  |  | NUMBER OF RECORDS IN FILE |

## APT3F.FD

### APT3F - RECORD, declared A27, computed 27

TEMPORARY A/P JOB # INDEX

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | A3JOB | D4 | D4 |  | JOB NUMBER |
| 4 | A3VND | D4 | D4 |  | VENDOR NUMBER |
| 8 | A3IDT | D8 | D8 |  | INVOICE DATE |
| 16 | A3VCH | D6 | D6 |  | VOUCHER NUMBER |
| 22 | A3REC | D5 | D5 |  | RECORD NUMBER |

### A3CTL - RECORD, computed 27 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A22 |  |  |  |
| 22 | A3NUM | D5 |  |  | NUMBER OF RECORDS IN FILE |

## APT4F.FD

### APT4F - RECORD, declared A11, computed 11

TEMP INDEX FOR 1099 REPORT

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | A4TYP | A2 | A2 |  | 1099 TYPE |
| 2 | A4VND | D4 | D4 |  | VENDOR NUMBER |
| 6 | A4REC | D5 | D5 |  | RECORD NUMBER |

## ARGL.FD

### ARGL1 - RECORD, declared A20, computed 20

RECORD #1 A/R TO G/L

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | ARCSH | D10 | D10.2 |  | A/R CASH |
| 10 | ARDSC | D10 | D10.2 |  | DISCOUNTS ALLOWED |

### ARGL2 - RECORD, computed 20 bytes

RECORD #2 A/R TO G/L

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | ARARO | D10 | D10.2 |  | A/R OPEN |
| 10 | ARSLS | D10 | D10.2 |  | SALES |

### ARGL3 - RECORD, computed 20 bytes

RECORD #3 A/R TO G/L

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | ARCRM | D10 | D10.2 |  | CREDIT MEMOS |
| 10 | ARDBM | D10 | D10.2 |  | DEBIT MEMOS |

### ARGL4 - RECORD, computed 20 bytes

RECORD #4 A/R TO G/L

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | ARFCH | D10 | D10.2 |  | FINANCE CHARGES |
| 10 | AROTH | D10 | D10.2 |  | OTHER CHARGES |

### ARGL5 - RECORD, computed 20 bytes

RECORD #5 A/R TO G/L

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | ARSTX | D10 | D10.2 |  | SALES TAX |
| 10 | ARFRT | D10 | D10.2 |  | FREIGHT |

### ARGL - RECORD, computed 20 bytes

RECORDS #6 TO MAX # RECORDS

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | ARAMT | D10 | D10.2 |  | G/L AMOUNT |
| 10 | ARACT | D7 | D7 |  | G/L ACCOUNT # |
| 17 | *(filler)* | A3 |  |  |  |

## AROP2.FD

### AROP2 - RECORD, declared A1838, computed 1838

A/R OPEN FILE (AROP2.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | RSDNO | D6 | D6 |  | DOCUMENT NUMBER |
| 6 | RSDTP | D1 | D1 |  | DOCUMENT TYPE |
| 7 | RSDDT | D8 | D8 |  | DOCUMENT DATE |
| 15 | RSCNO | A5 | A5 |  | CUSTOMER NUMBER |
| 20 | RSAMT | D8 | D8 |  | AMOUNT |
| 28 | RSOTH | D7 | D7 |  | OTHER AMT (MIS,TAX,FRT) |
| 35 | RSMSC | D6 | D6 |  | MISC. AMOUNT |
| 41 | RSTAX | D7 | D7 |  | SALES TAX |
| 48 | RSFRT | D6 | D6 |  | FREIGHT AMOUNT |
| 54 | RSAPL | D6 | D6 |  | APPLY TO NUMBER |
| 60 | RSSLS | D2 | D2 |  | SALESMAN NUMBER |
| 62 | RSJOB | D6 | D6 |  | NUMBER OF JOBS |
| 68 | RSCAT | 30D7 | A210 |  | CATEGORY |
| 278 | RSCQT | 30D6 | A180 |  | CATEGORY QUANTITY |
| 458 | RSDSC | 30A30 | A900 |  | DISCRIPTION |
| 1358 | RSCPR | 30D7 | A210 |  | CATEGORY PRICE |
| 1568 | RSCCT | 30D7 | A210 |  | CATEGORY COST |
| 1778 | RSDIS | 30D2 | A60 |  | DISCOUNT |

### RSCTL - RECORD, computed 1838 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1820 |  |  |  |
| 1820 | RSORG | D5 |  |  | ORGANIZE COUNT |
| 1825 | RSREC | D5 |  |  | RECORD COUNT |
| 1830 | RSMAX | D5 |  |  | MAXIMUM COUNT |
| 1835 | RSDEL | D3 |  |  | DELETE COUNT |

## AROPN.FD

### AROPN - RECORD, declared A1838, computed 1838

A/R OPEN FILE (AROPN.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | RODNO | D6 | D6 |  | DOCUMENT NUMBER |
| 6 | RODTP | D1 | D1 |  | DOCUMENT TYPE |
| 7 | RODDT | D8 | D8 |  | DOCUMENT DATE |
| 15 | ROCNO | A5 | A5 |  | CUSTOMER NUMBER |
| 20 | ROAMT | D8 | D8 |  | AMOUNT |
| 28 | ROOTH | D7 | D7 |  | OTHER AMT (MISC,TAX,FRT) |
| 35 | ROMSC | D6 | D6 |  | MISC AMOUNT |
| 41 | ROTAX | D7 | D7 |  | SALES TAX |
| 48 | ROFRT | D6 | D6 |  | FREIGHT |
| 54 | ROAPL | D6 | D6 |  | APPLY TO NUMBER |
| 60 | ROSLS | D2 | D2 |  | SALESMAN NUMBER |
| 62 | ROJOB | D6 | D6 |  | NUMBER OF JOBS |
| 68 | ROCAT | 30D7 | A210 |  | CATEGORYS |
| 278 | ROCQT | 30D6 | A180 |  | CATEGORY QUANTITY |
| 458 | RODSC | 30A30 | A900 |  | DISCRIPTION |
| 1358 | ROCPR | 30D7 | A210 |  | CATEGORY PRICE |
| 1568 | ROCCT | 30D7 | A210 |  | CATEGORY COST |
| 1778 | RODIS | 30D2 | A60 |  | DISCOUNT |

### (overlay 1) - RECORD, computed 20 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A15 |  |  |  |
| 15 | ROCN2 | A5 |  |  | CUSTOMER NUMBER AS ALPHA |

### ROCTL - RECORD, computed 1838 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1818 |  |  |  |
| 1818 | RODFG | D1 |  |  | DELETE FLAG |
| 1819 | ROSFG | D1 |  |  | SORT FLAG |
| 1820 | ROORG | D5 |  |  | ORGANIZE COUNT |
| 1825 | ROREC | D5 |  |  | RECORD COUNT |
| 1830 | ROMAX | D5 |  |  | MAXIMUM COUNT |
| 1835 | RODEL | D3 |  |  | DELETE COUNT |

## ASLIX.FD

### ASLIX - RECORD, declared A12, computed 12

A/R CUSTOMER AGED REPORTS INDEX (ASLIX.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | ASSLS | D2 | D2 |  | SALESMAN NUMBER |
| 2 | ASCNO | A5 | A5 |  | CUSTOMER NUMBER |
| 7 | ASRNO | D5 | D5 |  | RECORD NUMBER |

## ATWRK.FD

### ATWRK - RECORD, declared A58, computed 58

AUTO TRX WORK FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | AWACT | D7 | D7 |  | G/L ACCOUNT NUMBER |
| 7 | *(filler)* | A8 |  |  |  |
| 15 | AWAMT | D10 | D10.2 |  | TRANSACTION AMOUNT |
| 25 | AWSRC | A3 | A3 |  | TRANSACTION SRC |
| 28 | AWREF | A30 | A30 |  | TRANSACTION REFERENCE |

### AWCTL - RECORD, computed 58 bytes

AUTO TRX WORK FILE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A30 |  |  |  |
| 30 | AWBAL | D10 | D10.2 |  | TRANSACTION BALANCE |
| 40 | AWORG | D5 | D5 |  | ORGANIZED COUNT |
| 45 | AWREC | D5 | D5 |  | RECORD COUNT |
| 50 | AWMAX | D5 | D5 |  | MAXIMUM # OF RECORDS |
| 55 | AWDEL | D3 | D3 |  | DELETE COUNT |

## BIDDL.FD

### BIDDL - RECORD, declared A120, computed 120

BID MASTER FILE DELETION FILE	(BIDDL.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | BLACC | A5 | A5 |  | ACCOUNT NUMBER |
| 5 | BLPRD | D5 | D5 |  | PRODUCT NUMBER XX-XXX |
| 10 | BLDTE | D8 | D8 |  | DATE |
| 18 | BLBID | D7 | D7 |  | BID AMOUNT |
| 25 | BLDSC | A30 | A30 |  | STATEMENT DISCRIPTION |
| 55 | BLSPC | A65 | A65 |  | BID SPECS |

## BIDMS.FD

### BIDMS - RECORD, declared A120, computed 120

BID MASTER FILE	(BIDMS.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | BDACC | A5 | A5 |  | ACCOUNT NUMBER |
| 5 | BDPRD | D5 | D5 |  | PRODUCT NUMBER XX-XXX |
| 10 | BDDTE | D8 | D8 |  | DATE |
| 18 | BDBID | D7 | D7 |  | BID AMOUNT |
| 25 | BDDSC | A30 | A30 |  | STATEMENT DISCRIPTION |
| 55 | BDSPC | A65 | A65 |  | BID SPECS |

### (overlay 1) - RECORD, computed 120 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | BDKEY | A10 |  |  |  |
| 10 | *(filler)* | A110 |  |  | SLUSH |

## BIDMS.FDC

### BIDMS - COMMON, declared A120, computed 120

BID MASTER FILE	(BIDMS.FDC)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | BDACC | A5 | A5 |  | ACCOUNT NUMBER |
| 5 | BDPRD | D5 | D5 |  | PRODUCT NUMBER XX-XXX |
| 10 | BDDTE | D8 | D8 |  | DATE |
| 18 | BDBID | D7 | D7 |  | BID AMOUNT |
| 25 | BDDSC | A30 | A30 |  | STATEMENT DISCRIPTION |
| 55 | BDSPC | A65 | A65 |  | BID SPECS |

### (overlay 1) - COMMON, computed 120 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | BDKEY | A10 |  |  |  |
| 10 | *(filler)* | A110 |  |  | SLUSH |

## CASH.FD

### CASH - RECORD, declared A80, computed 80

CASH RECEIPTS FILE (CASH.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | CSCNO | A5 | A5 |  | CUSTOMER NUMBER |
| 5 | CSCNM | A25 | A25 |  | CUSTOMER NAME |
| 30 | CSRDT | D8 | D8 |  | RECEIPT DATE |
| 38 | CSCKN | D6 | D6 |  | CHECK NUMBER |
| 44 | CSAMT | D8 | D8 |  | AMOUNT RECEIVED |
| 52 | CSDIS | D7 | D7 |  | DISCOUNT AMOUNT |
| 59 | CSAPL | D6 | D6 |  | APPLY TO NUMBER |
| 65 | CSMSC | D8 | D8 |  | MISC AMOUNT |
| 73 | CSGLA | D7 | D7 |  | GENERAL LEDGER NUMBER |

### CSCTL - RECORD, computed 80 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A62 |  |  |  |
| 62 | CSORG | D5 |  |  | ORGANIZE COUNT |
| 67 | CSREC | D5 |  |  | RECORD COUNT |
| 72 | CSMAX | D5 |  |  | MAXIMUM COUNT |
| 77 | CSDEL | D3 |  |  | DELETE COUNT |

## CATMS.FDC

### CATMS - COMMON, declared A152, computed 152

PROC/CATEG MASTER FILE (CATMS.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | CTM10 | D7 |  |  | PRODUCT/CATEGORY NUMBER |
| 7 | CTM20 | A30 |  |  | PRDUCT DESCRIPTION |
| 37 | CTM30 | D4 |  |  | COST PERCENT |
| 41 | CTM40 | A15 |  |  | STATEMENT DESCRIPTION |
| 56 | CTM45 | D8 |  |  | QTY SOLD MTD |
| 64 | CTM50 | D9 |  |  | QTY SOLD YTD |
| 73 | CTM55 | D8 |  |  | SALES MTD |
| 81 | CTM60 | D9 |  |  | SALES YTD |
| 90 | CTM65 | D8 |  |  | COST MTD |
| 98 | CTM70 | D9 |  |  | COST YTD |
| 107 | CTM80 | D7 |  |  | G/L NUMBER SALES |
| 114 | CTM81 | D7 |  |  | G/L NUMBER COST |
| 121 | CTM82 | D7 |  |  | G/L NUMBER INVENTORY |
| 128 | CTM90 | D8 |  |  | QTY SOLD DAILY |
| 136 | CTM91 | D8 |  |  | SALES DAILY |
| 144 | CTM92 | D8 |  |  | COST DAILY |

## CHEKS.FD

### CHEKS - RECORD, declared A101, computed 101

CHECKS PRINTED FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | CKVND | D4 | D4 |  | VENDOR NUMBER |
| 4 | CKNAM | A25 | A25 |  | VENDOR NAME |
| 29 | CKINO | A35 | A35 |  | INVOICE NUMBER |
| 64 | CKIDT | D8 | D8 |  | INVOICE DATE |
| 72 | CKAMT | D10 | D10.2 |  | AMOUNT PAID |
| 82 | CKDPD | D8 | D8 |  | DATE PAID |
| 90 | CKCHK | D6 | D6 |  | CHECK NUMBER |
| 96 | CKJOB | D4 | D4 |  | JOB NUMBER |
| 100 | CKFLG | D1 | D1 |  | CLEAR FLAG |

### CKCTL - RECORD, computed 101 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A83 |  |  |  |
| 83 | CKORG | D5 |  |  |  |
| 88 | CKREC | D5 |  |  |  |
| 93 | CKMAX | D5 |  |  |  |
| 98 | CKDEL | D3 |  |  |  |

## CHKIX.FD

### CHKIX - RECORD, declared A13, computed 13

TEMP A/P CHECK HISTORY INDEX

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | CKCNO | D8 | D8 |  | CHECK NUMBER OR DATE |
| 8 | CKRNO | D5 | D5 |  | REC # IN CHECK FILE |

## CHKMS.FD

### CHKMS - RECORD, declared A101, computed 101

TEMP A/P CHECK HISTORY INDEX BY MISC

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | CIVND | D4 | D4 |  | VENDOR NUMBER |
| 4 | CINAM | A25 | A25 |  | VENDOR NAME |
| 29 | CIINO | A35 | A35 |  | INVOICE NUMBER |
| 64 | CIIDT | D8 | D8 |  | INVOICE DATE |
| 72 | CIAMT | D10 | D10.2 |  | AMOUNT PAID |
| 82 | CIDPD | D8 | D8 |  | DATE PAID |
| 90 | CICHK | D6 | D6 |  | CHECK NUMBER |
| 96 | CIJOB | D4 | D4 |  | JOB NUMBER |
| 100 | CIFLG | D1 | D1 |  | CLEAR FLAG |

## CITY.FD

### CITY - RECORD, declared A14, computed 14

MTD CITY TAX AMOUNT (CITY.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | CTAMT | D10 | D10 |  | CITY TAX AMOUNT |
| 10 | CTPER | D4 | D4 |  | CITY TAX PERCENT |

## CMFILE.FD

### CMFILE - RECORD, declared A81, computed 60  **MISMATCH**

COMPANY FILE FOR CONSOLIDATION (CMFILE.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | CTAB | 20D3 |  |  | TABLE BREAKDOWN |

## COFILE.FD

### TYPE1 - RECORD, declared A200, computed 200

COFILE RECORD DEFINITON

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | TABLE | 100D2 |  |  | COMPANY FILE TABLE |

### (overlay 1) - RECORD, computed 200 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | CFTAB | 100D2 |  |  | COMPANY FILE TABLE |

### TYPE2 - RECORD, declared A200, computed 200

COFILE RECORD DEFINITON

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | NUMBER | D2 |  |  | COMPANY NUMBER |
| 2 | NAME | A35 |  |  | COMPANY NAME |
| 37 | *(filler)* | A107 |  |  | FILLER |
| 144 | TYPPRT | A1 |  |  |  |
| 145 | *(filler)* | A55 |  |  | FILLER |

### (overlay 3) - RECORD, computed 200 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | CFNBR | D2 |  |  | COMPANY NUMBER |
| 2 | CFNAM | A35 |  |  | COMPANY NAME |
| 37 | CFAD1 | A35 |  |  | ADDRESS LINE 1 |
| 72 | CFAD2 | A35 |  |  | ADDRESS LINE 2 |
| 107 | CFAD3 | A35 |  |  | ADDRESS LINE 3 |
| 142 | CFACS | D2 |  |  | ACCESS |
| 144 | CFPTP | A1 |  |  | PRINTER TYPE |
| 145 | CFPFG | D1 |  |  | PRINTER CONTROL |
| 146 | CFCGL | A1 |  |  | CONSOLIDATED G/L FLAG |
| 147 | CFIPC | A1 |  |  | INTERFACE WITH PROFIT CENTER FLAG |
| 148 | CFPHN | A14 |  |  | PHONE NUMBER |
| 162 | CFSFN | A1 |  |  | S=SS#, F=FID#, BLANK |
| 163 | CFFID | A9 |  |  | FED # OR SS # |
| 172 | *(filler)* | A28 |  |  | SLUSH |

## COFILE.FDC

### TYPE1 - COMMON, declared A200, computed 200

COFILE RECORD DEFINITON

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | TABLE | 100D2 |  |  | COMPANY FILE TABLE |

### (overlay 1) - COMMON, computed 200 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | CFTAB | 100D2 |  |  | COMPANY FILE TABLE |

### TYPE2 - COMMON, declared A200, computed 200

COFILE RECORD DEFINITON

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | NUMBER | D2 |  |  | COMPANY NUMBER |
| 2 | NAME | A35 |  |  | COMPANY NAME |
| 37 | *(filler)* | A107 |  |  | FILLER |
| 144 | TYPPRT | A1 |  |  |  |
| 145 | *(filler)* | A55 |  |  | FILLER |

### (overlay 3) - COMMON, computed 200 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | CFNBR | D2 |  |  | COMPANY NUMBER |
| 2 | CFNAM | A35 |  |  | COMPANY NAME |
| 37 | CFAD1 | A35 |  |  | ADDRESS LINE 1 |
| 72 | CFAD2 | A35 |  |  | ADDRESS LINE 2 |
| 107 | CFAD3 | A35 |  |  | ADDRESS LINE 3 |
| 142 | CFACS | D2 |  |  | ACCESS |
| 144 | CFPTP | A1 |  |  | PRINTER TYPE |
| 145 | CFPFG | D1 |  |  | PRINTER CONTROL |
| 146 | CFCGL | A1 |  |  | CONSOLIDATED G/L FLAG |
| 147 | CFIPC | A1 |  |  | INTERFACE WITH PROFIT CENTER FLAG |
| 148 | CFPHN | A14 |  |  | PHONE NUMBER |
| 162 | CFSFN | A1 |  |  | S=SS#, F=FID#, BLANK |
| 163 | CFFID | A9 |  |  | FED # OR SS # |
| 172 | *(filler)* | A28 |  |  | SLUSH |

## CRTPY.FD

### CRTPY - RECORD, declared A1984, computed 1984

CERTIFIED TYPE FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | CPJOB | D4 | D4 |  | JOB NUMBER |
| 4 | CPDSC | 99A15 |  |  | CERTIFIED DESCRIPTION		99A15 |
| 1489 | CPRRT | 99D5 |  |  | CERTIFIED REGULAR RATE	99D5.3 |

### CPFCT - RECORD, computed 1984 bytes

CERTIFIED TYPE FILE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1971 |  |  |  |
| 1971 | CPFRC | D5 |  |  | RECORD COUNT |
| 1976 | CPFMX | D5 |  |  | MAXIMUM # RECORDS |
| 1981 | CPFDC | D3 |  |  | DELETE COUNT |

## CRTWK.FD

### CRTWK - RECORD, declared A89, computed 89

CERTIFIED WORK FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | CWJOB | D4 | D4 |  | JOB  NUMBER |
| 4 | CWEMP | D4 | D4 |  | EMPLOYEE NUMBER |
| 8 | CWDSC | A15 | A15 |  | CERTIFCATION TYPE DESC |
| 23 | CWRGR | D5 | D5.3 |  | REGULAR RATE |
| 28 | CWOTR | D5 | D5.3 |  | O.T. RATE |
| 33 | CWRGH | 7D4 | D28 |  | REGULAR HOURS |
| 61 | CWOTH | 7D4 | D28 |  | O.T. HOURS |

## CSCIX.FD

### CSCIX - RECORD, declared A12, computed 12

CUSTOMER CATEGORY SALES INDEX (CSCIX.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | CCCNO | A5 | A5 |  | CUSTOMER NUMBER |
| 5 | CCSLS | D2 | D2 |  | SALESMAN NUMBER |
| 7 | CCRNO | D5 | D5 |  | RECORD NUMBER |

## CSLCN.FD

### CSLCN - RECORD, declared A37, computed 37

CONSOLIDATED COMPANY NUMBER FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | CCNUM | D2 | D2 |  | COMPANY NUMBER |
| 2 | CCNAM | A35 | A35 |  | COMPANY NAME |

### CCCTL - RECORD, computed 37 bytes

CONSOLIDATED COMPANY NUMBER FILE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A17 |  |  |  |
| 17 | CCCON | D2 | D2 |  | # OF COMPANIES ALREADY CONSOLIDATED |
| 19 | CCORG | D5 | D5 |  | ORGANIZED COUNT |
| 24 | CCREC | D5 | D5 |  | RECORD COUNT |
| 29 | CCMAX | D5 | D5 |  | MAXIMUM # OF RECORDS |
| 34 | *(filler)* | A3 |  |  |  |

## CSLFX.FD

### CSLFX - RECORD, declared A23, computed 23

CONSOLIDATED FIN. STMT INDEX

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | CFACT | D7 | D7 |  | G/L ACCOUNT NUMBER |
| 7 | CFFSC | A7 | A7 |  | FINANCIAL STATEMENT CODE |
| 14 | CFMAS | D4 | D4 |  | RECORD # IN CONSOLIDATED G/L MASTER |
| 18 | CFREC | D5 | D5 |  | RECORD # OF 1ST TRX IN CON. YTD FILE |

## CSLIX.FD

### CSLIX - RECORD, declared A11, computed 11

CONSOLIDATED G/L MASTER FILE INDEX

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | CXACT | D7 | D7 |  | G/L ACCOUNT NUMBER |
| 7 | CXREC | D4 | D4 |  | RECORD # IN CONSOL. G/L MASTER FILE |

## CSLMS.FD

### CSLMS - RECORD, declared A296, computed 296

CONSOLIDATED G/L MASTER FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | CGACT | D7 | D7 |  | G/L ACCOUNT NUMBER |
| 7 | CGDSC | A30 | A30 |  | G/L ACCOUNT DESCRIPTION |
| 37 | CGFSC | A7 | A7 |  | FINANCIAL STATEMENT CODE |
| 44 | CGSSC | A7 | A7 |  | SUPPORTING SCHEDULE CODE |
| 51 | CGPRN | A1 | A1 |  | PARENTHESIS CONTROL |
| 52 | CGBDG | 13D8 | D104 |  | BUDGET AMOUNTS |
| 156 | CGCMP | 14D10 | D140 |  | PRIOR YEAR COMPARATIVES |

### CGCTL - RECORD, computed 296 bytes

CONSOLIDATED G/L MASTER FILE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | CGSDT | 13D8 | D104 |  | STARTING PERIOD DATES |
| 104 | CGEDT | 13D8 | D104 |  | ENDING PERIOD DATES |
| 208 | *(filler)* | A70 |  |  |  |
| 278 | CGORG | D5 | D5 |  | ORGANIZED COUNT |
| 283 | CGREC | D5 | D5 |  | RECORD COUNT |
| 288 | CGMAX | D5 | D5 |  | MAXIMUM # OF RECORDS |
| 293 | CGDEL | D3 | D3 |  | DELETE COUNT |

## CSLSX.FD

### CSLSX - RECORD, declared A16, computed 16

CONSOLIDATED SUPP. SCHED. INDEX

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | CSSSC | A7 | A7 |  | SUPPORTING SCHEDULE CODE |
| 7 | CSMAS | D4 | D4 |  | RECORD # IN CON. G/L MASTER FILE |
| 11 | CSREC | D5 | D5 |  | RECORD # OF 1ST TRX IN CON. YTD FILE |

## CSLTF.FD

### CSLTF - RECORD, declared A66, computed 66

CONSOLIDATED G/L TEMPORARY FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | CLCSL | D11 | D11.2 |  | CURRENT PERIOD SALES |
| 11 | CLYSL | D11 | D11.2 |  | YTD SALES |
| 22 | CLCCS | D11 | D11.2 |  | CURRENT PRD BUDGETED/COMPARED SALES |
| 33 | CLYCS | D11 | D11.2 |  | YTD BUDGETED/COMPARED SALES |
| 44 | CLYPL | D11 | D11.2 |  | YTD PROFIT/LOSS |
| 55 | CLCPL | D11 | D11.2 |  | LAST YEAR'S PROFIT/LOSS |

## CSLYD.FD

### CSLYD - RECORD, declared A59, computed 59

CONSOLIDATED YTD TRX FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | CYACT | D7 | D7 |  | G/L ACCOUNT NUMBER |
| 7 | CYDAT | D8 | D8 |  | TRX DATE |
| 15 | CYAMT | D11 | D11.2 |  | TRX AMOUNT |
| 26 | CYSRC | A3 | A3 |  | TRX SOURCE |
| 29 | CYREF | A30 | A30 |  | TRX REFERENCE |

### CYCTL - RECORD, computed 59 bytes

CONSOLIDATED YTD TRX FILE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A4 |  |  |  |
| 4 | CYSPD | D2 | D2 |  | STARTING PERIOD |
| 6 | CYEPD | D2 | D2 |  | ENDING PERIOD |
| 8 | CYSDT | D8 | D8 |  | STARTING DATE |
| 16 | CYEDT | D8 | D8 |  | ENDING DATE |
| 24 | CYPFC | D3 | D3 |  | PROFIT CENTER |
| 27 | CYCMP | D1 | D1 |  | COMPARISON FLAG |
| 28 | CYBSF | D1 | D1 |  | BALANCE SHEET FLAG |
| 29 | CYSSF | D1 | D1 |  | SUPPORTING SCHEDULE FLAG |
| 30 | CYMON | D2 | D2 |  | MONTH PREVIOUS TO STARTING DATE |
| 32 | CYDAY | D2 | D2 |  | DAY PREVIOUS TO STARTING DATE |
| 34 | CYYR | D4 | D4 |  | YEAR PREVIOUS TO STARTING DATE |
| 38 | *(filler)* | A21 |  |  |  |

## CTRAC.FD

### CTRAC - RECORD, declared A96, computed 96

CUSTOMER TRACE FILE (CTRAC.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | CTCDE | D1 | D1 |  | TRACE CODE |
| 1 | CTCNO | A5 | A5 |  | CUSTOMER NUMBER |
| 6 | CTCNM | A25 | A25 |  | CUSTOMER NAME |
| 31 | CTSLS | D2 | D2 |  | SALESMAN NUMBER |
| 33 | CTSMD | D8 | D8 |  | SALES MTD |
| 41 | CTCMD | D8 | D8 |  | COST MTD |
| 49 | CTSYD | D9 | D9 |  | SALES YTD |
| 58 | CTCYD | D8 | D8 |  | COST YTD |
| 66 | *(filler)* | A30 | A30 |  | SLUSH |

### (overlay 1) - RECORD, computed 96 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A31 | A31 |  | SLUSH |
| 31 | CTDSC | A15 | A15 |  | CHANGE DESCRIPTION |
| 46 | CTOLD | A25 | A25 |  | OLD INFORMATION |
| 71 | CTNEW | A25 | A25 |  | NEW INFORMATION |

### CTCTL - RECORD, computed 96 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A78 |  |  |  |
| 78 | CTORG | D5 |  |  | ORGANIZE COUNT |
| 83 | CTREC | D5 |  |  | RECORD COUNT |
| 88 | CTMAX | D5 |  |  | MAXIMUM COUNT |
| 93 | CTDEL | D3 |  |  | DELETE COUNT |

## CUSIX.FD

### CUSIX - RECORD, declared A30, computed 30

CUSTOMER INDEX (CUSIX.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | CIX05 | A25 |  |  | SHORT NAME |
| 25 | CIX10 | A5 |  |  | ACCOUNT NUMBER |

### (overlay 1) - RECORD, computed 30 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | CIKEY | A30 |  |  |  |

## CUSMS.FDC

### CUSMS - COMMON, declared A313, computed 313

CUSTOMER MASTER FILE (CUSMS.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | CMNUM | A5 | A5 |  | CUSTOMER NUMBER |
| 5 | CMNAM | A25 | A25 |  | CUSTOMER NAME |
| 30 | CMAD1 | A25 | A25 |  | CUSTOMER ADDRESS LINE 1 |
| 55 | CMAD2 | A25 | A25 |  | CUSTOMER ADDRESS LINE 2 |
| 80 | CMCTY | A15 | A15 |  | CITY |
| 95 | CMSTE | A2 | A2 |  | STATE |
| 97 | CMZIP | A9 | A9 |  | ZIP CODE |
| 106 | CMSHT | A25 | A25 |  | SHORT NAME |
| 131 | CMSLS | D2 | D2 |  | SALESMAN NUMBER |
| 133 | CMCTP | A2 | A2 |  | CUSTOMER TYPE |
| 135 | CMSMD | D8 | D8 |  | SALES MTD |
| 143 | CMSYD | D9 | D9 |  | SALES YTD |
| 152 | CMCMD | D8 | D8 |  | COST MTD |
| 160 | CMCYD | D8 | D8 |  | COST YTD |
| 168 | CMTXF | A1 | A1 |  | TAX FLAG |
| 169 | CMCRD | D6 | D6 |  | CREDIT LIMIT |
| 175 | CMBMT | D1 | D1 |  | BALANCE METHOD |
| 176 | CMSTF | D1 | D1 |  | STATEMENT FLAG |
| 177 | CMDIS | D2 | D2 |  | DISCOUNT PERCENTAGE |
| 179 | CMCTX | D3 | D3 |  | CITY TAX PERCENTAGE |
| 182 | CMCCD | D3 | D3 |  | CITY TAX CODE |
| 185 | CMSY1 | D9 | D9 |  | SALES PRIOR YEAR 1 |
| 194 | CMCY1 | D8 | D8 |  | COST PRIOR YEAR 1 |
| 202 | CMSY2 | D9 | D9 |  | SALES PRIOR YEAR 2 |
| 211 | CMCY2 | D8 | D8 |  | COST PRIOR YEAR 2 |
| 219 | CMACD | D3 | D3 |  | AREA CODE |
| 222 | CMHPN | D7 | D7 |  | HOME PHONE NUMBER |
| 229 | CMWPN | D7 | D7 |  | WORK PHONE NUMBER |
| 236 | CMDPU | D8 | D8 |  | DATE LAST PURCHASED |
| 244 | CMDPY | D8 | D8 |  | DATE LAST PAID |
| 252 | CMAPY | D8 | D8 |  | AMOUNT LAST PAID |
| 260 | CMFCD | D1 | D1 |  | FINANCE CODE |
| 261 | CMDEN | D6 | D6 |  | DATE ENTERED |
| 267 | CMPRM | D2 | D2 |  | PRICE MATRIX CODE |
| 269 | CMOVC | A1 | A1 |  | PRICE OVERRIDE CODE |
| 270 | CMCON | A15 | A15 |  | CONTACT PERSON |
| 285 | CMTEX | A15 | A15 |  | TAX EXEMPT # |
| 300 | CMPCD | D1 | D1 |  | PRICE CODE 1-4 |
| 301 | CMBRK | A1 | A1 |  | QTY BREAK Y OR N |
| 302 | CMLNO | A2 | A2 |  | LAST PAST DUE LETTER # |
| 304 | CMLDT | D8 | D8 |  | DATE LAST PAST DUE LETTER |
| 312 | CMLFG | A1 | A1 |  | PAST DUE LETTER FLAG |

## DEVICE.FD

### DEVREC - RECORD, computed 127 bytes

DEVICE FILE RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | DF005 | A4 |  |  | FILE ID |
| 4 | DF010 | A50 |  |  | FILE NAME |
| 54 | DF015 | A40 |  |  | FILE DESCRIPTION |
| 94 | DF020 | A1 |  |  | JUSTIFICATION FLAG: |
| 95 | DF025 | A25 |  |  | KEY DESCRIPTION |
| 120 | DF030 | D2 |  |  | KEY LENGTH |
| 122 | DF035 | D2 |  |  | LINE OF KEY |
| 124 | DF040 | D3 |  |  | COLUMN OF KEY |

## DFDATA.FD

### DFDAT - COMMON, computed 70 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | DFFID | A4 |  |  | FILE ID |
| 4 | DFRDS | D2 |  |  | NUMBER OF READERS (-1 IF READ/WRITE PROTECTED) |
| 6 | DFWRS | D2 |  |  | NUMBER OF WRITERS (-1 IF WRITE PROTECTED) |
| 8 | DFFIL | A50 |  |  | FILE NAME |
| 58 | DFRS | D5 |  |  | RECORD SIZE |
| 63 | DFBS | D2 |  |  | BUCKET SIZE |
| 65 | DFAL | D5 |  |  | ALLOCATION |

### (overlay 1) - COMMON, computed 82 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | DFCMP | D2 |  |  | COMPANY NUMBER BEING USED |
| 2 | DFTBL | 15A4 |  |  | OPEN FILE TABLE |
| 62 | DFTCD | 15A1 |  |  | OPEN FILE MODE TABLE |
| 77 | DFREC | D5 |  |  | RECORD NUMBER OF FID IN DEVICE FILE |

## DFDATA.FDC

### DFDAT - COMMON, computed 70 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | DFFID | A4 |  |  | FILE ID |
| 4 | DFRDS | D2 |  |  | NUMBER OF READERS (-1 IF READ/WRITE PROTECTED) |
| 6 | DFWRS | D2 |  |  | NUMBER OF WRITERS (-1 IF WRITE PROTECTED) |
| 8 | DFFIL | A50 |  |  | FILE NAME |
| 58 | DFRS | D5 |  |  | RECORD SIZE |
| 63 | DFBS | D2 |  |  | BUCKET SIZE |
| 65 | DFAL | D5 |  |  | ALLOCATION |

### (overlay 1) - COMMON, computed 82 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | DFCMP | D2 |  |  | COMPANY NUMBER BEING USED |
| 2 | DFTBL | 15A4 |  |  | OPEN FILE TABLE |
| 62 | DFTCD | 15A1 |  |  | OPEN FILE MODE TABLE |
| 77 | DFREC | D5 |  |  | RECORD NUMBER OF FID IN DEVICE FILE |

## EQPMF.FD

### EQPMF - RECORD, computed 96 bytes

EQUIPMENT COST MASTER FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | EQPNO | D5 |  |  | EQUIPMENT NUMBER BALANCE BROUGHT FORWARD |
| 5 | EDESC | A25 |  |  | NOT USED FOR DESCRIPTION, USED TO MARK FOR DELETION |
| 30 | ERFLD | D9 |  |  | REPAIR FIELD BALANCE BROUGHT FORWARD |
| 39 | ELSHP | D9 |  |  | LABOR SHOP BALANCE BROUGHT FORWARD |
| 48 | EPSSH | D9 |  |  | PARTS AND SERVICE SHOP BALANCE BROUGHT FORWARD |
| 57 | EPSDL | D9 |  |  | PARTS AND SERVICE DEALERS BALANCE BROUGHT FORWARD |
| 66 | EFOL | D9 |  |  | FUEL, OIL, LUBE BALANCE BROUGHT FORWARD |
| 75 | EOPHR | D9 |  |  | OPERATING HOURS BALANCE BROUGHT FORWARD |
| 84 | EOPRT | D7 |  |  | OPERATING RATE |
| 91 | EDTHR | D5 |  |  | DOWN TIME HOURS (CURRENTLY NOT USED - JULY 1982) |

### EMFCT - RECORD, computed 96 bytes

EQUIPMENT COST MASTER FILE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A76 |  |  |  |
| 76 | EMFSF | D1 |  |  | SORT FLAG |
| 77 | EMFDF | D1 |  |  | DELETE FLAG |
| 78 | EMFOC | D5 |  |  | ORGANIZED COUNT |
| 83 | EMFRC | D5 |  |  | RECORD COUNT |
| 88 | EMFMX | D5 |  |  | MAXIMUM RECORD COUNT |
| 93 | EMFDC | D3 |  |  | DELETE COUNT |

## EQPMF.FDC

### EQPMF - COMMON, computed 96 bytes

EQUIPMENT COST MASTER FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | EQPNO | D5 |  |  | EQUIPMENT NUMBER BALANCE BROUGHT FORWARD |
| 5 | EDESC | A25 |  |  | NOT USED FOR DESCRIPTION, USED TO MARK FOR DELETION |
| 30 | ERFLD | D9 |  |  | REPAIR FIELD BALANCE BROUGHT FORWARD |
| 39 | ELSHP | D9 |  |  | LABOR SHOP BALANCE BROUGHT FORWARD |
| 48 | EPSSH | D9 |  |  | PARTS AND SERVICE SHOP BALANCE BROUGHT FORWARD |
| 57 | EPSDL | D9 |  |  | PARTS AND SERVICE DEALERS BALANCE BROUGHT FORWARD |
| 66 | EFOL | D9 |  |  | FUEL, OIL, LUBE BALANCE BROUGHT FORWARD |
| 75 | EOPHR | D9 |  |  | OPERATING HOURS BALANCE BROUGHT FORWARD |
| 84 | EOPRT | D7 |  |  | OPERATING RATE |
| 91 | EDTHR | D5 |  |  | DOWN TIME HOURS (CURRENTLY NOT USED - JULY 1982) |

### EMFCT - COMMON, computed 96 bytes

EQUIPMENT COST MASTER FILE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A76 |  |  |  |
| 76 | EMFSF | D1 |  |  | SORT FLAG |
| 77 | EMFDF | D1 |  |  | DELETE FLAG |
| 78 | EMFOC | D5 |  |  | ORGANIZED COUNT |
| 83 | EMFRC | D5 |  |  | RECORD COUNT |
| 88 | EMFMX | D5 |  |  | MAXIMUM RECORD COUNT |
| 93 | EMFDC | D3 |  |  | DELETE COUNT |

## EQPTF.FD

### EQPTF - RECORD, computed 99 bytes

EQUIPMENT COST TRANSACTION FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | ETEQP | D5 |  |  | EQUIPMENT COST NUMBER |
| 5 | ETRFL | D9 |  |  | REPAIR FIELD |
| 14 | ETLSH | D9 |  |  | LABOR SHOP |
| 23 | ETPSS | D9 |  |  | PARTS & SERVICE SHOP |
| 32 | ETPSD | D9 |  |  | PARTS & SERVICE DEALERS |
| 41 | ETFOL | D9 |  |  | FUEL-OIL-LUBE |
| 50 | ETOHR | D9 |  |  | OPERATING HOURS |
| 59 | ETDAT | D8 |  |  | DATE |
| 67 | ETREF | A30 |  |  | REFERENCE |
| 97 | ETSRC | A2 |  |  | SOURCE |

### ETFCT - RECORD, computed 99 bytes

EQUIPMENT COST TRANSACTION FILE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A86 |  |  |  |
| 86 | ETFRC | D5 |  |  | RECORD COUNT |
| 91 | ETFMX | D5 |  |  | MAXIMUM # RECORDS |
| 96 | *(filler)* | A3 |  |  |  |

## EQPTF.FDC

### EQPTF - COMMON, computed 99 bytes

EQUIPMENT COST TRANSACTION FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | ETEQP | D5 |  |  | EQUIPMENT COST NUMBER |
| 5 | ETRFL | D9 |  |  | REPAIR FIELD |
| 14 | ETLSH | D9 |  |  | LABOR SHOP |
| 23 | ETPSS | D9 |  |  | PARTS & SERVICE SHOP |
| 32 | ETPSD | D9 |  |  | PARTS & SERVICE DEALERS |
| 41 | ETFOL | D9 |  |  | FUEL-OIL-LUBE |
| 50 | ETOHR | D9 |  |  | OPERATING HOURS |
| 59 | ETDAT | D8 |  |  | DATE |
| 67 | ETREF | A30 |  |  | REFERENCE |
| 97 | ETSRC | A2 |  |  | SOURCE |

### ETFCT - COMMON, computed 99 bytes

EQUIPMENT COST TRANSACTION FILE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A86 |  |  |  |
| 86 | ETFRC | D5 |  |  | RECORD COUNT |
| 91 | ETFMX | D5 |  |  | MAXIMUM # RECORDS |
| 96 | *(filler)* | A3 |  |  |  |

## FINCH.FD

### FINCH - RECORD, declared A31, computed 31

FINANCE CHARGE WORK FILE (FINCH.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | FCDDT | D8 | D8 |  | DATE |
| 8 | FCCNO | A5 | A5 |  | CUSTOMER NUMBER |
| 13 | FCODA | D8 | D8 |  | OVERDUE AMOUNT |
| 21 | FCCAM | D7 | D7 |  | CHARGED AMOUNT |
| 28 | FCSLS | D2 | D2 |  | SALESMAN NUMBER |
| 30 | FCBMT | D1 | D1 |  | BALANCE METHOD |

## GLAIX.FD

### GLAIX - RECORD, declared A11, computed 11

G/L MASTER FILE INDEX

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | GIACT | D7 | D7 |  | G/L ACCOUNT NUMBER |
| 7 | GIREC | D4 | D4 |  | RECORD # IN ACCOUNT MASTER |

## GLAIX.FDC

### GLAIX - COMMON, declared A11, computed 11

G/L MASTER FILE INDEX

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | GIACT | D7 | D7 |  | G/L ACCOUNT NUMBER |
| 7 | GIREC | D4 | D4 |  | RECORD # IN ACCOUNT MASTER |

## GLAM2.FD

### GLAMS2 - RECORD, declared A296, computed 296

G/L MASTER FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | GMACT2 | D7 | D7 |  | G/L ACCOUNT NUMBER |
| 7 | GMDSC2 | A30 | A30 |  | G/L ACCOUNT DESCRIPTION |
| 37 | GMFSC2 | A7 | A7 |  | FINANCIAL STATEMENT CODE |
| 44 | GMSSC2 | A7 | A7 |  | SUPPORTING SCHEDULE CODE |
| 51 | GMPRN2 | A1 | A1 |  | DEBIT OR CREDIT ACCOUNT |
| 52 | GMBDG2 | 13D8 |  |  | BUDGET AMOUNTS			13D8 |
| 156 | GMCMP2 | 14D10 |  |  | COMPARATIVE AMOUNTS		14D10.2 |

### GMCTL2 - RECORD, computed 296 bytes

G/L MASTER FILE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | GMSDT2 | 13D8 |  |  | ACCOUNTING PERIOD START DATES	13D8 |
| 104 | GMEDT2 | 13D8 |  |  | ACCOUNTING PERIOD END DATES	13D8 |
| 208 | *(filler)* | A52 |  |  |  |
| 260 | GMPSD2 | D8 | D8 |  | PRV PRD START DATE |
| 268 | GMPED2 | D8 | D8 |  | PRV PRD END DATE |
| 276 | GMDFG2 | D1 | D1 |  | DELETE FLAG (1=DO NOT PURGE) |
| 277 | GMSFG2 | D1 | D1 |  | SORT FLAG (1=DO NOT SORT) |
| 278 | GMORG2 | D5 | D5 |  | ORGANIZED COUNT |
| 283 | GMREC2 | D5 | D5 |  | RECORD COUNT |
| 288 | GMMAX2 | D5 | D5 |  | MAXIMUM # OF RECORDS |
| 293 | GMDEL2 | D3 | D3 |  | DELETE COUNT |

## GLAMS.FD

### GLAMS - RECORD, declared A296, computed 296

G/L MASTER FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | GMACT | D7 | D7 |  | G/L ACCOUNT NUMBER |
| 7 | GMDSC | A30 | A30 |  | G/L ACCOUNT DESCRIPTION |
| 37 | GMFSC | A7 | A7 |  | FINANCIAL STATEMENT CODE |
| 44 | GMSSC | A7 | A7 |  | SUPPORTING SCHEDULE CODE |
| 51 | GMPRN | A1 | A1 |  | DEBIT OR CREDIT ACCOUNT |
| 52 | GMBDG | 13D8 |  |  | BUDGET AMOUNTS			13D8 |
| 156 | GMCMP | 14D10 |  |  | COMPARATIVE AMOUNTS		14D10.2 |

### GMCTL - RECORD, computed 296 bytes

G/L MASTER FILE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | GMSDT | 13D8 |  |  | ACCOUNTING PERIOD START DATES	13D8 |
| 104 | GMEDT | 13D8 |  |  | ACCOUNTING PERIOD END DATES	13D8 |
| 208 | *(filler)* | A52 |  |  |  |
| 260 | GMPSD | D8 | D8 |  | PRV PRD START DATE |
| 268 | GMPED | D8 | D8 |  | PRV PRD END DATE |
| 276 | GMDFG | D1 | D1 |  | DELETE FLAG (1=DO NOT PURGE) |
| 277 | GMSFG | D1 | D1 |  | SORT FLAG (1=DO NOT SORT) |
| 278 | GMORG | D5 | D5 |  | ORGANIZED COUNT |
| 283 | GMREC | D5 | D5 |  | RECORD COUNT |
| 288 | GMMAX | D5 | D5 |  | MAXIMUM # OF RECORDS |
| 293 | GMDEL | D3 | D3 |  | DELETE COUNT |

## GLAMS.FDC

### GLAMS - COMMON, declared A296, computed 296

G/L MASTER FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | GMACT | D7 | D7 |  | G/L ACCOUNT NUMBER |
| 7 | GMDSC | A30 | A30 |  | G/L ACCOUNT DESCRIPTION |
| 37 | GMFSC | A7 | A7 |  | FINANCIAL STATEMENT CODE |
| 44 | GMSSC | A7 | A7 |  | SUPPORTING SCHEDULE CODE |
| 51 | GMPRN | A1 | A1 |  | DEBIT OR CREDIT ACCOUNT |
| 52 | GMBDG | 13D8 |  |  | BUDGET AMOUNTS			13D8 |
| 156 | GMCMP | 14D10 |  |  | COMPARATIVE AMOUNTS		14D10.2 |

### GMCTL - COMMON, computed 296 bytes

G/L MASTER FILE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | GMSDT | 13D8 |  |  | ACCOUNTING PERIOD START DATES	13D8 |
| 104 | GMEDT | 13D8 |  |  | ACCOUNTING PERIOD END DATES	13D8 |
| 208 | *(filler)* | A68 |  |  |  |
| 276 | GMDFG | D1 | D1 |  | DELETE FLAG (1=DO NOT PURGE) |
| 277 | GMSFG | D1 | D1 |  | SORT FLAG (1=DO NOT SORT) |
| 278 | GMORG | D5 | D5 |  | ORGANIZED COUNT |
| 283 | GMREC | D5 | D5 |  | RECORD COUNT |
| 288 | GMMAX | D5 | D5 |  | MAXIMUM # OF RECORDS |
| 293 | GMDEL | D3 | D3 |  | DELETE COUNT |

## GLDIS.FD

### GLDIS - RECORD, declared A80, computed 80

G/L DISTRIBUTION FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | GDACT | D7 | D7 |  | G/L ACCOUNT # |
| 7 | GDVCH | D6 | D6 |  | VOUCHER NUMBER |
| 13 | GDVND | D4 | D4 |  | VENDOR NUMBER |
| 17 | GDINO | A35 | A35 |  | INVOICE NUMBER |
| 52 | GDDAT | D8 | D8 |  | INVOICE DATE |
| 60 | GDAMT | D10 | D10.2 |  | AMOUNT |
| 70 | *(filler)* | A10 | A10 |  | SLUSH   (NEEDED FOR SORT) |

### GDCTL - RECORD, computed 80 bytes

G/L DISTRIBUTION FILE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A16 |  |  |  |
| 16 | GDINT | D1 |  |  | INTERFACE FLAG |
| 17 | GDDTL | D1 |  |  | INTERFACE W/DETAIL=1 |
| 18 | *(filler)* | A44 |  |  |  |
| 62 | GDORG | D5 | D5 |  | ORGANIZED COUNT |
| 67 | GDREC | D5 | D5 |  | RECORD COUNT |
| 72 | GDMAX | D5 | D5 |  | MAXIMUM # OF RECORDS |
| 77 | *(filler)* | A3 |  |  |  |

## GLIFL.FD

### GLIFL - RECORD, declared A77, computed 77

INTERFACE FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | GFACT | D7 | D7 |  | ACCOUNT NUMBER |
| 7 | GFDAT | D8 | D8 |  | TRX DATE |
| 15 | GFAMT | D10 | D10.2 |  | TRX AMOUNT |
| 25 | GFSRC | A3 | A3 |  | TRX SOURCE |
| 28 | GFREF | A30 | A30 |  | TRX REFERENCE |
| 58 | *(filler)* | A19 | A19 |  | SLUSH (JOB COST) |

### GFCTL - RECORD, computed 77 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A59 |  |  |  |
| 59 | GFORG | D5 |  |  |  |
| 64 | GFREC | D5 |  |  |  |
| 69 | GFMAX | D5 |  |  |  |
| 74 | *(filler)* | A3 |  |  |  |

## GLINT.FD

### GLINT - RECORD, declared A185, computed 185

G/L INTERFACE FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | GNSYS | 3D1 |  |  | SYSTEMS TO BE INTERFACED (1=A/R,2=A/P,3=PR)	3D1 |
| 3 | GNARC | D7 | D7 |  | A/R CASH (IN) ACCOUNT # |
| 10 | GNDSA | D7 | D7 |  | DISCOUNTS ALLOWED ACCOUNT # |
| 17 | GNARO | D7 | D7 |  | A/R OPEN ACCOUNT # |
| 24 | GNSLS | D7 | D7 |  | SALES ACCOUNT # |
| 31 | GNCRM | D7 | D7 |  | CREDIT MEMOS ACCOUNT # |
| 38 | GNDBM | D7 | D7 |  | DEBIT MEMOS ACCOUNT # |
| 45 | GNFCH | D7 | D7 |  | FINANCE CHARGES ACCOUNT # |
| 52 | GNOTH | D7 | D7 |  | OTHER CHARGES ACCOUNT # |
| 59 | GNSTX | D7 | D7 |  | SALES TAX ACCOUNT # |
| 66 | GNFRT | D7 | D7 |  | FREIGHT ACCOUNT # |
| 73 | GNAPC | D7 | D7 |  | A/P CASH (OUT)	ACCOUNT # |
| 80 | GNDST | D7 | D7 |  | DISCOUNTS TAKEN ACCOUNT # |
| 87 | GNAPO | D7 | D7 |  | A/P OPEN ACCOUNT # |
| 94 | GNPRC | D7 | D7 |  | PR CASH (OUT) ACCOUNT # |
| 101 | *(filler)* | A84 | A84 |  | SLUSH |

## GLPFC.FD

### GLPFC - RECORD, declared A15, computed 15

G/L PROFIT CENTER FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | GPDSC | A15 | A15 |  | PROFIT CENTER DESCRIPTION |

## GLSCH.FD

### GLSCH - RECORD, declared A32, computed 32

SUPPORTING SCHEDULE FILES

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | GSACT | D7 | D7 |  | ACCOUNT NUMBER |
| 7 | GSSSC | A7 | A7 |  | SUPPORTING SCHEDULE CODE |
| 14 | *(filler)* | A18 | A18 |  | SLUSH |

### GSCTL - RECORD, computed 32 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A14 |  |  |  |
| 14 | GSORG | D5 |  |  |  |
| 19 | GSREC | D5 |  |  |  |
| 24 | GSMAX | D5 |  |  |  |
| 29 | GSDEL | D3 |  |  |  |

## GLT1F.FD

### GLT1F - RECORD, declared A276, computed 276

TEMPORARY FILE FOR 12-MONTH COMPARATIVE REPORT

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | G1SLS | 14D10 | A140 |  | SALES PER PERIOD OR YTD & GRAND TOTAL |
| 140 | G1NAM | A35 | A35 |  | COMPANY NAME |
| 175 | G1SNO | D2 | D2 |  | CURRENT SCHEDULE NUMBER TO PRINT |
| 177 | G1SCH | 99D1 | A99 |  | SCHEDULES SELECTED TO PRINT |

### (overlay 1) - RECORD, computed 276 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | G1PFT | 14D10 | A140 |  | PROFIT/LOSS PER PERIOD OR YTD & GRAND TOTAL |
| 140 | *(filler)* | A136 |  |  |  |

## GLTIX.FD

### GLTIX - RECORD, declared A18, computed 18

G/L MASTER FILE TEMPORARY INDEX

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | GTACT | D7 | D7 |  | G/L ACCOUNT NUMBER |
| 7 | GTREC | D4 | D4 |  | RECORD # IN ACCOUNT MASTER FILE |
| 11 | GTFSC | A7 | A7 |  | FINANCIAL STATEMENT CODE |

## GLWRK.FD

### GLWRK - RECORD, declared A77, computed 77

G/L WORK FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | GWACT | D7 | D7 |  | G/L ACCOUNT NUMBER |
| 7 | GWDAT | D8 | D8 |  | TRANSACTION DATE |
| 15 | GWAMT | D10 | D10 |  | TRANSACTION AMOUNT |
| 25 | GWSRC | A3 | A3 |  | TRANSACTION SOURCE |
| 28 | GWREF | A30 | A30 |  | TRANSACTION REFERENCE |
| 58 | GWJOB | D7 | D7 |  | JOB COST NUMBER |
| 65 | GWUNT | D3 | D3 |  | UNIT COST NUMBER |
| 68 | GWEQP | D5 | D5 |  | EQUIPMENT COST NUMBER |
| 73 | GWECD | D1 | D1 |  | EQUIPMENT COST CODE |
| 74 | *(filler)* | A3 | A3 |  | SLUSH |

### GWCTL - RECORD, computed 77 bytes

G/L WORK FILE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A49 |  |  |  |
| 49 | GWBAL | D10 | D10.2 |  | TRX BALANCE |
| 59 | GWORG | D5 | D5 |  | ORGANIZED COUNT |
| 64 | GWREC | D5 | D5 |  | RECORD COUNT |
| 69 | GWMAX | D5 | D5 |  | MAXIMUM # OF RECORDS |
| 74 | *(filler)* | A3 |  |  |  |

## GLWRK.FDC

### GLWRK - COMMON, declared A77, computed 77

G/L WORK FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | GWACT | D7 | D7 |  | G/L ACCOUNT NUMBER |
| 7 | GWDAT | D8 | D8 |  | TRANSACTION DATE |
| 15 | GWAMT | D10 | D10 |  | TRANSACTION AMOUNT |
| 25 | GWSRC | A3 | A3 |  | TRANSACTION SOURCE |
| 28 | GWREF | A30 | A30 |  | TRANSACTION REFERENCE |
| 58 | GWJOB | D7 | D7 |  | JOB COST NUMBER |
| 65 | GWUNT | D3 | D3 |  | UNIT COST NUMBER |
| 68 | GWEQP | D5 | D5 |  | EQUIPMENT COST NUMBER |
| 73 | GWECD | D1 | D1 |  | EQUIPMENT COST CODE |
| 74 | *(filler)* | A3 | A3 |  | SLUSH |

### GWCTL - COMMON, computed 77 bytes

G/L WORK FILE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A49 |  |  |  |
| 49 | GWBAL | D10 | D10.2 |  | TRX BALANCE |
| 59 | GWORG | D5 | D5 |  | ORGANIZED COUNT |
| 64 | GWREC | D5 | D5 |  | RECORD COUNT |
| 69 | GWMAX | D5 | D5 |  | MAXIMUM # OF RECORDS |
| 74 | *(filler)* | A3 |  |  |  |

## HEADER.FDC

### HDRMS - COMMON, declared A1000, computed 1000

HEADER FILE (HEADER.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | HD001 | A1 |  |  | SALES ENTRY CATEGORY BREAKDONW FLAG |
| 1 | HD002 | D3 |  |  | DAYS PAST DUE F/C |
| 4 | HD003 | D4 |  |  | S/C PERCENT |
| 8 | HD004 | D6 |  |  | MINIMUN S/C CALULATION |
| 14 | HD005 | D6 |  |  | MINIMUN S/C AMOUNT |
| 20 | HD006 | D3 |  |  | DAYS PAST DUE PAST DUE AGING |
| 23 | HD007 | A1 |  |  | PRINT ZERO BAL STATEMENTS Y OR N |
| 24 | HD008 | A1 |  |  | PRINT NEGATIVE STATEMENTS |
| 25 | HD009 | D6 |  |  | SKIP STATEMNETS BELOW THIS |
| 31 | HD010 | A1 |  |  | SKIP ZERO SALES IN SALES ANALYSIS REPORTS |
| 32 | HD011 | A1 |  |  | SHOW CUST MEASURMENTS |
| 33 | HD012 | A1 |  |  | USE 1/3 DUE CONCEPT |
| 34 | HD013 | D4 |  |  | MIN DUE % |
| 38 | HD014 | A1 |  |  | UPDATE CUSTOMER TRACE FILE |
| 39 | HD015 | A1 |  |  | UPDATE AROPEN WITH DETAIL |
| 40 | HD016 | A1 |  |  | USE DEF CASH SALE SALESMAN |
| 41 | HD017 | D2 |  |  | DEFAULT CASH SALE SALESMAN |
| 43 | HD018 | A1 |  |  | USE DEF SALESMAN VS MASTER |
| 44 | HD019 | D2 |  |  | DEFAULT SALESMAN |
| 46 | HD020 | A1 |  |  | USE MASTEER CITY-STATE |
| 47 | HD021 | D3 |  |  | DEFAULT CITY CODE |
| 50 | HD022 | A2 |  |  | DEFAULT STATE CODE |
| 52 | HD023 | A1 |  |  | AUTO CALCULATE SALES TAX |
| 53 | HD024 | D7 |  |  | DEFAULT CAT # |
| 60 | HD025 | A1 |  |  | ENTER LAST 4 OF CATEGORY |
| 61 | HD026 | A1 |  |  | DISPLAY COST |
| 62 | HD027 | A1 |  |  | COST TO USE |
| 63 | HD028 | D4 |  |  | STANDARD COST PERCENT |
| 67 | HD029 | A1 |  |  | PRINT TICKETS |
| 68 | HD030 | A1 |  |  | BUMP DOC # IN SALES ENTRY |
| 69 | HD031 | A1 |  |  | PRINT CAT INFO ON EDIT LIST AND JOUNAL |
| 70 | HD100 | A1 |  |  | QUANTITY TO BE DEC/WHOLE |
| 71 | HD101 | A1 |  |  | USE SPECIAL ITEMS |
| 72 | HD102 | A1 |  |  | USE DEFAULT CASH SALE SALESMAN |
| 73 | HD103 | D2 |  |  | DEFAULT CASH SALE SALESMAN |
| 75 | HD104 | A1 |  |  | USE DEFAULT SALESMAN VS MASTER |
| 76 | HD105 | D2 |  |  | DEFAULT SALESMAN |
| 78 | HD106 | A1 |  |  | PRINT INVOICES |
| 79 | HD107 | A1 |  |  | COST BASIS - L = LIFO  A = AVERAGE COST |
| 80 | HD108 | A1 |  |  | INV WINDOW # DISPLAY - P = PRICE  C = COST |
| 81 | HD109 | A1 |  |  | WRITE TO TRACE FILE Y OR N |
| 82 | HD110 | A5 |  |  | DEFAULT CUSTOMER NUMBER - TICKET ENTRY |
| 87 | HD111 | D1 |  |  | DEFAULT CUSTOMER TYPE - TICKET ENTRY |
| 88 | HD112 | A1 |  |  | PRINT DETL SLS JRNL BY SLSMN  (Y OR N) |
| 89 | HD200 | A1 |  |  | UPDATE G/L |
| 90 | HD201 | A1 |  |  | UPDATE CUSTOMER CATEGORY |
| 91 | HD202 | A1 |  |  | UPDATE SALEMAN CATEGORY |
| 92 | HD203 | A1 |  |  | UPDATE PRODUCT CATEGORY |
| 93 | HD204 | D7 |  |  | G/L # - GENERAL BANK ACCOUNT |
| 100 | HD205 | D7 |  |  | G/L # - GENERAL SALES ACCOUNT |
| 107 | HD206 | D7 |  |  | G/L # - GENERAL COST OF GOODS ACCOUNT |
| 114 | HD207 | D7 |  |  | G/L # - GENERAL INVENTORY ACCOUNT |
| 121 | HD208 | D7 |  |  | G/L # - GENERAL F/C ACCOUNT |
| 128 | HD209 | D7 |  |  | G/L # - GENERAL A/R ACCOUNT |
| 135 | HD210 | D7 |  |  | G/L # - GENERAL MISC ACCOUNT |
| 142 | HD211 | D7 |  |  | G/L # - GENERAL FREIGHT |
| 149 | HD212 | D7 |  |  | G/L # - GENERAL DISCOUNT |
| 156 | *(filler)* | A844 |  |  |  |

## JOBAF.FD

### JOBAF - RECORD, declared A33, computed 33

JOB ACTIVITY DESCRIPTION FILE -

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | JANUM | D3 | D3 |  | ACTIVITY NUMBER |
| 3 | JADSC | A30 | A30 |  | ACTIVITY DESCRIPTION |

### JAFCT - RECORD, computed 33 bytes

JOB ACTIVITY DESCRIPTION FILE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A13 |  |  | A14 |
| 13 | JAFDF | D1 | D1 |  | DELETE FLAG |
| 14 | JAFSF | D1 | D1 |  | SORT FLAG |
| 15 | JAFOC | D5 | D5 |  | ORGANIZED COUNT |
| 20 | JAFRC | D5 | D5 |  | RECORD COUNT |
| 25 | JAFMX | D5 | D5 |  | MAXIMUM # RECORDS |
| 30 | JAFDC | D3 | D3 |  | DELETE COUNT |

## JOBCD.FD

### JOBCD - RECORD, declared A65, computed 65

JOB COST CURRENT PERIOD DETAIL FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | JCJOB | D7 | D7 |  | JOB NUMBER |
| 7 | JCGLA | D7 | D7 |  | G/L ACCOUNT NUMBER |
| 14 | JCDAT | D8 | D8 |  | DATE |
| 22 | JCDSC | A30 | A30 |  | DESCRIPTION |
| 52 | JCAMT | D10 | D10.2 |  | AMOUNT OF TRX |
| 62 | JCSRC | A2 | A2 |  | SOURCE OF TRX |
| 64 | JCCOD | A1 | A1 |  | TRX CODE (A OR H) |

### JCDCT - RECORD, computed 65 bytes

JOB COST CURRENT PERIOD DETAIL FILE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A52 |  |  |  |
| 52 | JCDRC | D5 |  |  | RECORD COUNT |
| 57 | JCDMX | D5 |  |  | MAXIMUM RECORD COUNT |
| 62 | *(filler)* | A3 |  |  |  |

## JOBDF.FD

### JOBDF - RECORD, declared A50, computed 50

JOB NUMBER DESCRIPTION FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | JDNUM | D4 | D4 |  | JOB NUMBER |
| 4 | JDDSC | A30 | A30 |  | JOB DESCRIPTION |
| 34 | JDCRT | A1 | A1 |  | CERTIFIED CODE |
| 35 | JDDLR | D10 | D10.2 |  | $ PAID TO JOB |
| 45 | JDBRD | D5 | D5.2 |  | BURDEN PERCENT |

### JDFCT - RECORD, computed 50 bytes

JOB NUMBER DESCRIPTION FILE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A30 |  |  |  |
| 30 | JDFDF | D1 |  |  | DELETE FLAG |
| 31 | JDFSF | D1 |  |  | SORT FLAG |
| 32 | JDFOC | D5 |  |  | ORGANIZED COUNT |
| 37 | JDFRC | D5 |  |  | RECORD COUNT |
| 42 | JDFMX | D5 |  |  | MAXIMUM # OF RECORDS |
| 47 | JDFDC | D3 |  |  | DELETE COUNT |

## JOBHS.FD

### JOBHS - RECORD, declared A65, computed 65

JOB COST HISTORY FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | JHJOB | D7 | D7 |  | JOB NUMBER |
| 7 | JHGLA | D7 | D7 |  | G/L ACCOUNT NUMBER |
| 14 | JHDAT | D8 | D8 |  | DATE |
| 22 | JHDSC | A30 | A30 |  | DESCRIPTION |
| 52 | JHAMT | D10 | D10.2 |  | AMOUNT OF TRX |
| 62 | JHSRC | A2 | A2 |  | SOURCE OF TRX |
| 64 | JHCOD | A1 | A1 |  | TRX CODE (A OR H) |

### JHSCT - RECORD, computed 65 bytes

JOB COST HISTORY FILE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A52 |  |  |  |
| 52 | JHREC | D5 |  |  | RECORD COUNT |
| 57 | JHMAX | D5 |  |  | MAXIMUM RECORD COUNT |
| 62 | *(filler)* | A3 |  |  |  |

## JOBMF.FD

### JOBMF - RECORD, declared A104, computed 104

JOB COST MASTER FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | JOBNO | D7 | D7 |  | JOB NUMBER |
| 7 | JEDOL | D10 | D10.2 |  | ESTIMATE ORGINAL DOLLARS |
| 17 | JERVD | D10 | D10.2 |  | ESTIMATE REVISED DOLLARS |
| 27 | JDTDR | D8 | D8 |  | DATE $ REVISED |
| 35 | JCURD | D10 | D10.2 |  | CURRENT PERIOD DOLLARS |
| 45 | JPTDD | D10 | D10.2 |  | PROJECT TO DATE DOLLARS |
| 55 | JBHRS | D10 | D10.2 |  | BUDGET HOURS |
| 65 | JBRVH | D10 | D10.2 |  | BUDGET HOURS REVISED |
| 75 | JDTHR | D8 | D8 |  | DATE HOURS REVISED |
| 83 | JCURH | D10 | D10.2 |  | HOURS CURRENT PERIOD |
| 93 | JPTDH | D10 | D10.2 |  | HOURS PROJECT TO DATE |
| 103 | JCOMP | A1 | A1 |  | PROJECT COMPLETE Y OR N |

### JMFCT - RECORD, computed 104 bytes

JOB COST MASTER FILE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A84 |  |  |  |
| 84 | JMFSF | D1 |  |  | SORT FLAG |
| 85 | JMFDF | D1 |  |  | DELETE FLAG |
| 86 | JMFOC | D5 |  |  | ORGANIZED COUNT |
| 91 | JMFRC | D5 |  |  | RECORD COUNT |
| 96 | JMFMX | D5 |  |  | MAXIMUM RECORD COUNT |
| 101 | JMFDC | D3 |  |  | DELETE COUNT |

## JOBMF.FDC

### JOBMF - COMMON, declared A104, computed 104

JOB COST MASTER FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | JOBNO | D7 | D7 |  | JOB NUMBER |
| 7 | JEDOL | D10 | D10.2 |  | ESTIMATE ORGINAL DOLLARS |
| 17 | JERVD | D10 | D10.2 |  | ESTIMATE REVISED DOLLARS |
| 27 | JDTDR | D8 | D8 |  | DATE $ REVISED |
| 35 | JCURD | D10 | D10.2 |  | CURRENT PERIOD DOLLARS |
| 45 | JPTDD | D10 | D10.2 |  | PROJECT TO DATE DOLLARS |
| 55 | JBHRS | D10 | D10.2 |  | BUDGET HOURS |
| 65 | JBRVH | D10 | D10.2 |  | BUDGET HOURS REVISED |
| 75 | JDTHR | D8 | D8 |  | DATE HOURS REVISED |
| 83 | JCURH | D10 | D10.2 |  | HOURS CURRENT PERIOD |
| 93 | JPTDH | D10 | D10.2 |  | HOURS PROJECT TO DATE |
| 103 | JCOMP | A1 | A1 |  | PROJECT COMPLETE Y OR N |

### JMFCT - COMMON, computed 104 bytes

JOB COST MASTER FILE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A84 |  |  |  |
| 84 | JMFSF | D1 |  |  | SORT FLAG |
| 85 | JMFDF | D1 |  |  | DELETE FLAG |
| 86 | JMFOC | D5 |  |  | ORGANIZED COUNT |
| 91 | JMFRC | D5 |  |  | RECORD COUNT |
| 96 | JMFMX | D5 |  |  | MAXIMUM RECORD COUNT |
| 101 | JMFDC | D3 |  |  | DELETE COUNT |

## JOBTF.FD

### JOBTF - RECORD, computed 65 bytes

JOB COST TRANSACTION FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | JTJOB | D7 |  |  | JOB NUMBER |
| 7 | JTGLA | D7 |  |  | G/L ACCOUNT NUMBER |
| 14 | JTDAT | D8 |  |  | TRX DATE |
| 22 | JTDSC | A30 |  |  | DESCRIPTION |
| 52 | JTAMT | D10 |  |  | TRX DOLLAR AMOUNT |
| 62 | JTSRC | A2 |  |  | SOURCE OF TRANSACTION |
| 64 | JTCOD | A1 |  |  | ALWAYS AN 'A' FOR JOB COST AMOUNT |

### JTFCT - RECORD, computed 65 bytes

JOB COST TRANSACTION FILE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A36 |  |  |  |
| 36 | JTFFC | D5 | D5.2 |  | FICA % |
| 41 | *(filler)* | A11 |  |  |  |
| 52 | JTFRC | D5 |  |  | RECORD COUNT |
| 57 | JTFMX | D5 |  |  | MAXIMUM RECORD COUNT |
| 62 | *(filler)* | A3 |  |  |  |

### (overlay 2) - RECORD, computed 4 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | JTACT | D4 |  |  |  |

## JOBTF.FDC

### JOBTF - COMMON, computed 65 bytes

JOB COST TRANSACTION FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | JTJOB | D7 |  |  | JOB NUMBER |
| 7 | JTGLA | D7 |  |  | G/L ACCOUNT NUMBER |
| 14 | JTDAT | D8 |  |  | TRX DATE |
| 22 | JTDSC | A30 |  |  | DESCRIPTION |
| 52 | JTAMT | D10 |  |  | TRX DOLLAR AMOUNT |
| 62 | JTSRC | A2 |  |  | SOURCE OF TRANSACTION |
| 64 | JTCOD | A1 |  |  | ALWAYS AN 'A' FOR JOB COST AMOUNT |

### JTFCT - COMMON, computed 65 bytes

JOB COST TRANSACTION FILE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A52 |  |  |  |
| 52 | JTFRC | D5 |  |  | RECORD COUNT |
| 57 | JTFMX | D5 |  |  | MAXIMUM RECORD COUNT |
| 62 | *(filler)* | A3 |  |  |  |

### (overlay 2) - COMMON, computed 4 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | JTACT | D4 |  |  |  |

## JTRACE.FD

### JTRCE - RECORD, declared A104, computed 104

JOB MASTER FILE TRACE FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | TCODE | D1 | D1 |  | TRACE CODE |
| 1 | TJOB | D7 | D7 |  | JOB NUMBER |
| 8 | TEDOL | D10 | D10.2 |  | ORIGNAL ESTIMATE DOLLARS |
| 18 | TERVD | D10 | D10.2 |  | REVISED ESTIMATE DOLLARS |
| 28 | TDTDR | D8 | D8 |  | DATE $ REVISED |
| 36 | TCURD | D10 | D10.2 |  | CURRENT PERIOD DOLLARS |
| 46 | TPTDD | D10 | D10.2 |  | PROJECT TO DATE DOLLARS |
| 56 | TBHRS | D10 | D10.2 |  | BUDGET HOURS |
| 66 | TBRVH | D10 | D10.2 |  | BUDGET HOURS REVISED |
| 76 | TDTHR | D8 | D8 |  | DATE HOURS REVISED |
| 84 | TCURH | D10 | D10.2 |  | HOURS CURRENT PERIOD |
| 94 | TPTDH | D10 | D10.2 |  | HOURS PROJECT TO DATE |

### (overlay 1) - RECORD, computed 53 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A8 |  |  |  |
| 8 | TDESC | A25 |  |  | DESCRIPTION |
| 33 | TOLD | A10 |  |  | OLD DATA |
| 43 | TNEW | A10 |  |  | NEW DATA |

### JTRCT - RECORD, computed 104 bytes

JOB MASTER TRACE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A86 |  |  |  |
| 86 | JTROC | D5 |  |  | ORGANIZED COUNT |
| 91 | JTRRC | D5 |  |  | RECORD COUNT |
| 96 | JTRMX | D5 |  |  | MAXIMUM COUNT |
| 101 | *(filler)* | A3 |  |  |  |

## LETMS.FD

### LETMS - RECORD, declared A849, computed 849

PAST DUE LETTER FILE (LETMS.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | LM001 | 4A70 |  |  | PAST DUE LETTERS INFORMATION 1 |
| 280 | LM002 | 4A70 |  |  | PAST DUE LETTERS INFORMATION 2 |
| 560 | LM003 | 4A70 |  |  | PAST DUE LETTERS INFORMATION 3 |
| 840 | LM004 | D3 |  |  | PAST DUE LETTER 1 DAYS |
| 843 | LM005 | D3 |  |  | PAST DUE LETTER 2 DAYS |
| 846 | LM006 | D3 |  |  | PAST DUE LETTER 3 DAYS |

## MONCS.FD

### MONCS - RECORD, declared A40, computed 40

MONTHLY CASH FILE (MONCS.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | MCDTE | D8 | D8 |  | DATE |
| 8 | MCAMT | D9 | D9 |  | AMOUNT |
| 17 | MCMSC | D7 | D7 |  | MISC AMOUNT |
| 24 | MCDIS | D9 | D9 |  | DISCOUNT AMOUNT |
| 33 | MCGLA | D7 | D7 |  | GENERAL LEDGER ACCOUNT |

### MCCTL - RECORD, computed 40 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A22 |  |  |  |
| 22 | MCORG | D5 |  |  | ORGANIZE COUNT |
| 27 | MCREC | D5 |  |  | RECORD COUNT |
| 32 | MCMAX | D5 |  |  | MAXIMUM COUNT |
| 37 | MCDEL | D3 |  |  | DELETE COUNT |

## MONSL.FD

### MONSL - RECORD, declared A49, computed 49

MONTHLY SALES FILE (MONSL.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | MSDTE | D8 | D8 |  | DATE |
| 8 | MSAMT | D9 | D9 |  | AMOUNT |
| 17 | MSMSC | D7 | D7 |  | MISC AMOUNT |
| 24 | MSTAX | D8 | D8 |  | TAX AMOUNT |
| 32 | MSFRT | D7 | D7 |  | FREIGHT |
| 39 | MSTYP | D1 | D1 |  | TYPE |
| 40 | MSCST | D9 | D9 |  | COST |

### MSCTL - RECORD, computed 49 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A31 |  |  |  |
| 31 | MSORG | D5 |  |  | ORGANIZE COUNT |
| 36 | MSREC | D5 |  |  | RECORD COUNT |
| 41 | MSMAX | D5 |  |  | MAXIMUM COUNT |
| 46 | MSDEL | D3 |  |  | DELETE COUNT |

## MSVND.FD

### MSVND - RECORD, declared A108, computed 108

MISCELLANEOUS A/P VENDOR FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | MVVCH | D6 | D6 |  | VOUCHER NUMBER |
| 6 | MVNAM | A25 | A25 |  | VENDOR NAME |
| 31 | MVAD1 | A25 | A25 |  | ADDRESS LINE ONE |
| 56 | MVAD2 | A25 | A25 |  | ADDRESS LINE TWO |
| 81 | MVCTY | A15 | A15 |  | CITY |
| 96 | MVSTA | A2 | A2 |  | STATE |
| 98 | MVZIP | A9 | A9 |  | ZIP CODE |
| 107 | MVPDF | D1 | D1 |  | FLAG FOR PAID VOUCHERS |

### MVCTL - RECORD, computed 108 bytes

CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A90 |  |  |  |
| 90 | MVORG | D5 |  |  | ORGANIZED COUNT |
| 95 | MVREC | D5 |  |  | RECORD COUNT |
| 100 | MVMAX | D5 |  |  | MAXIMUM # OF RECORDS |
| 105 | MVDEL | D3 |  |  | DELETE COUNT |

## MSVND.FDC

### MSVND - COMMON, declared A108, computed 108

MISCELLANEOUS A/P VENDOR FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | MVVCH | D6 | D6 |  | VOUCHER NUMBER |
| 6 | MVNAM | A25 | A25 |  | VENDOR NAME |
| 31 | MVAD1 | A25 | A25 |  | ADDRESS LINE ONE |
| 56 | MVAD2 | A25 | A25 |  | ADDRESS LINE TWO |
| 81 | MVCTY | A15 | A15 |  | CITY |
| 96 | MVSTA | A2 | A2 |  | STATE |
| 98 | MVZIP | A9 | A9 |  | ZIP CODE |
| 107 | MVPDF | D1 | D1 |  | FLAG FOR PAID VOUCHERS |

### MVCTL - COMMON, computed 108 bytes

CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A90 |  |  |  |
| 90 | MVORG | D5 |  |  | ORGANIZED COUNT |
| 95 | MVREC | D5 |  |  | RECORD COUNT |
| 100 | MVMAX | D5 |  |  | MAXIMUM # OF RECORDS |
| 105 | MVDEL | D3 |  |  | DELETE COUNT |

## NEWAP.FD

### NEWAP - RECORD, declared A1019, computed 1019

NEW PAYABLES FILE (NEWAP.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | NPVCH | D6 | D6 |  | VOUCHER NUMBER |
| 6 | NPVND | D4 | D4 |  | VENDOR NUMBER |
| 10 | NPNAM | A25 | A25 |  | VENDOR NAME |
| 35 | NPINO | A35 | A35 |  | INVOICE NUMBER |
| 70 | NPIDT | D8 | D8 |  | INVOICE DATE |
| 78 | NPAMT | D10 | D10 |  | INVOICE AMOUNT |
| 88 | NPNDA | D10 | D10 |  | NON-DISCOUNTING AMOUNT |
| 98 | NPPCT | D3 | D3 |  | DISCOUNT PERCENT |
| 101 | NPDSC | D8 | D8 |  | DISCOUNT AMOUNT |
| 109 | NPDDT | D8 | D8 |  | DUE DATE |
| 117 | NPCHK | D6 | D6 |  | CHECK NUMBER |
| 123 | NPJNO | D4 | D4 |  | JOB NUMBER FOR A/P OPEN |
| 127 | NPACT | 27D7 | A189 |  | G/L EXPENSE ACCOUNT NUMBER |
| 316 | NPEXP | 27D10 | A270 |  | EXPENSE ACCOUNT AMOUNT |
| 586 | NPJOB | 27D7 | A189 |  | JOB COST NUMBER |
| 775 | NPUNT | 27D3 | A81 |  | UNIT COST NUMBER |
| 856 | NPEQP | 27D5 | A135 |  | EQUIPMENT COST NUMBER |
| 991 | NPECD | 27D1 | D27 |  | EQUIPMENT COST CODE |
| 1018 | *(filler)* | A1 | A1 |  | SLUSH |

### NPCTL - RECORD, computed 1019 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A10 |  |  |  |
| 10 | NPNXT | D6 |  |  | NEXT VOUCHER NUMBER |
| 16 | *(filler)* | A18 |  |  |  |
| 34 | NPINT | D1 |  |  | G/L INTERFACE FLAG |
| 35 | *(filler)* | A966 |  |  |  |
| 1001 | NPORG | D5 |  |  | ORGANIZE COUNT |
| 1006 | NPREC | D5 |  |  | RECORD COUNT |
| 1011 | NPMAX | D5 |  |  | MAXIMUM COUNT |
| 1016 | NPDEL | D3 |  |  | DELETE COUNT |

## NEWAP.FDC

### NEWAP - COMMON, declared A1019, computed 1019

NEW PAYABLES FILE (NEWAP.FDC)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | NPVCH | D6 | D6 |  | VOUCHER NUMBER |
| 6 | NPVND | D4 | D4 |  | VENDOR NUMBER |
| 10 | NPNAM | A25 | A25 |  | VENDOR NAME |
| 35 | NPINO | A35 | A35 |  | INVOICE NUMBER |
| 70 | NPIDT | D8 | D8 |  | INVOICE DATE |
| 78 | NPAMT | D10 | D10 |  | INVOICE AMOUNT |
| 88 | NPNDA | D10 | D10 |  | NON-DISCOUNTING AMOUNT |
| 98 | NPPCT | D3 | D3 |  | DISCOUNT PERCENT |
| 101 | NPDSC | D8 | D8 |  | DISCOUNT AMOUNT |
| 109 | NPDDT | D8 | D8 |  | DUE DATE |
| 117 | NPCHK | D6 | D6 |  | CHECK NUMBER |
| 123 | NPJNO | D4 | D4 |  | JOB NUMBER FOR A/P OPEN |
| 127 | NPACT | 27D7 | A189 |  | G/L EXPENSE ACCOUNT NUMBER |
| 316 | NPEXP | 27D10 | A270 |  | EXPENSE ACCOUNT AMOUNT |
| 586 | NPJOB | 27D7 | A189 |  | JOB COST NUMBER |
| 775 | NPUNT | 27D3 | A81 |  | UNIT COST NUMBER |
| 856 | NPEQP | 27D5 | A135 |  | EQUIPMENT COST NUMBER |
| 991 | NPECD | 27D1 | D27 |  | EQUIPMENT COST CODE |
| 1018 | *(filler)* | A1 | A1 |  | SLUSH |

### NPCTL - COMMON, computed 1019 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A10 |  |  |  |
| 10 | NPNXT | D6 |  |  | NEXT VOUCHER NUMBER |
| 16 | *(filler)* | A18 |  |  |  |
| 34 | NPINT | D1 |  |  | G/L INTERFACE FLAG |
| 35 | *(filler)* | A966 |  |  |  |
| 1001 | NPORG | D5 |  |  | ORGANIZE COUNT |
| 1006 | NPREC | D5 |  |  | RECORD COUNT |
| 1011 | NPMAX | D5 |  |  | MAXIMUM COUNT |
| 1016 | NPDEL | D3 |  |  | DELETE COUNT |

## NEWGL.FD

### NEWGL - RECORD, declared A80, computed 80

NEW G/L DISTRIBUTION FILE (NEWGL.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | NGACT | D7 | D7 |  | EXPENSE ACCOUNT NUMBER |
| 7 | NGVCH | D6 | D6 |  | VOUCHER NUMBER |
| 13 | NGVND | D4 | D4 |  | VENDOR NUMBER |
| 17 | NGINO | A35 | A35 |  | INVOICE NUMBER |
| 52 | NGIDT | D8 | D8 |  | INVOICE DATE |
| 60 | NGAMT | D10 | D10 |  | INVOICE AMOUNT |
| 70 | *(filler)* | A10 | A10 |  | SLUSH   (NEEDED FOR SORT) |

### NGCTL - RECORD, computed 80 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | NGAC2 | D7 |  |  | TEMPORARY ACCOUNT NUMBER |
| 7 | NGVC2 | D6 |  |  | TEMPORARY VOUCHER NUMBER |
| 13 | *(filler)* | A49 |  |  |  |
| 62 | NGORG | D5 |  |  | ORGANIZE COUNT |
| 67 | NGREC | D5 |  |  | RECORD COUNT |
| 72 | NGMAX | D5 |  |  | MAXIMUM COUNT |
| 77 | NGDEL | D3 |  |  | DELETE COUNT |

## PA20.FD

### PCTRL - RECORD, declared A500, computed 500

PA20.DDF RECORD DEFINITION

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PC005 | 14A9 | A126 |  | EARNINGS TYPE TAX TABLE.  ONE |
| 126 | PC010 | D8 | D8.0 |  | ENDING PYRL DATE FOR EARNINGS TYPE 1 |
| 134 | PC015 | D8 | D8.0 |  | ENDING PYRL DATE FOR EARNINGS TYPE 2 |
| 142 | PC020 | 10D1 | A10 |  | FREQUENCY CODES FOR THIS PAYROLL RUN |
| 152 | PC035 | D7 | D7.2 |  | FICA MAXIMUM YTD DEDUCTION |
| 159 | PC040 | D8 | D8.2 |  | FICA MAXIMUM YTD TAXABLE EARNINGS |
| 167 | PC045 | D3 | D3.2 |  | FICA TAX RATE (FORMAT X.XX%) |
| 170 | PC050 | D6 | D6.2 |  | EXEMPTION ALLOWANCE ON FED W/H |
| 176 | PC085 | D2 | D2.0 |  | MAXIMUM NUMBER OF LINES PER PAGE |
| 178 | PC090 | 9D2 | A18 |  | NUMBER OF PAY DAYS PER YEAR FOR |
| 196 | PC100 | D8 | D8.0 |  | CURRENT DATE IN USE FOR PAYROLL |
| 204 | PC105 | D2 | D2 |  | VAC PAY EARNINGS TYPE |
| 206 | PC110 | D2 | D2 |  | SICK PAY EARNINGS TYPE |
| 208 | PC120 | D5 | D5.3 |  | MINIMUM WAGE RATE |
| 213 | PC125 | A1 | A1 |  | UPDATE PAYROLL HISTORY FLAG |
| 214 | PC130 | A1 | A1 |  | W2'S TO MAGNETIC TAPE FLAG |
| 215 | PC135 | A1 | A1 |  | PRINT CHECK STUB ONLY FLAG |
| 216 | PC150 | A1 | A1 |  | PRINT CAFETERIA REPORTS |
| 217 | PC155 | A1 | A1 |  | ACCRUE VACATION FLAG |
| 218 | PC160 | D1 | D1 |  | VACATION FREQUENCY CODE |
| 219 | PC165 | D2 | D2 |  | MONTH VACATION ACCRUAL LAST RAN |
| 221 | *(filler)* | A3 | A3 |  | UNUSED SLUSH |
| 224 | PC495 | A1 | A1 |  | COMPANY STATUS |
| 225 | PC500 | A1 | A1 |  | JOB COST FLAG |
| 226 | PC505 | 99A1 | A99 |  | RATE, AMT, OR MILES DECISION TABLE |
| 325 | PC510 | A1 | A1 |  | FICA EARNINGS OPTION FLAG |
| 326 | PC515 | A8 | A8 |  | COMPANY NUMBER |
| 334 | PC520 | A30 | A30 |  | COMPANY NAME |
| 364 | PC525 | A25 | A25 |  | NAME/ADDRESS LINE 2 |
| 389 | PC530 | A25 | A25 |  | NAME/ADDRESS LINE 3 |
| 414 | PC535 | A15 | A15 |  | NAME/ADDRESS LINE 4 |
| 429 | PC540 | A2 | A2 |  | STATE CODE |
| 431 | PC545 | A9 | A9 |  | ZIP CODE |
| 440 | PC550 | A16 | A16 |  | FEDERAL ID NUMBER |
| 456 | PC565 | A1 | A1 |  | GENERAL LEDGER INTERFACE FLAG |
| 457 | PC570 | D7 | D7.2 |  | MEDICARE MAX YTD DEDUCTION |
| 464 | PC571 | D8 | D8.2 |  | MEDICARE MAXIMUM YTD TAXABLE EARNINGS |
| 472 | PC572 | D4 | D4.3 |  | MEDICARE TAX RATE |
| 476 | *(filler)* | A24 | A24 |  | SLUSH |

### (overlay 1) - RECORD, computed 126 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PC700 | 14D9 |  |  |  |

### ETTEL - RECORD, declared A9, computed 9

EARNINGS TYPE TABLE ELEMENT

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | TXFLG | 9D1 | A9 |  | THE 9 TAXABLE FLAGS FOR THIS |

## PA20.FDC

### PCTRL - COMMON, declared A500, computed 500

PA20.DDF RECORD DEFINITION

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PC005 | 14A9 | A126 |  | EARNINGS TYPE TAX TABLE.  ONE |
| 126 | PC010 | D8 | D8.0 |  | ENDING PYRL DATE FOR EARNINGS TYPE 1 |
| 134 | PC015 | D8 | D8.0 |  | ENDING PYRL DATE FOR EARNINGS TYPE 2 |
| 142 | PC020 | 10D1 | A10 |  | FREQUENCY CODES FOR THIS PAYROLL RUN |
| 152 | PC035 | D7 | D7.2 |  | FICA MAXIMUM YTD DEDUCTION |
| 159 | PC040 | D8 | D8.2 |  | FICA MAXIMUM YTD TAXABLE EARNINGS |
| 167 | PC045 | D3 | D3.2 |  | FICA TAX RATE (FORMAT X.XX%) |
| 170 | PC050 | D6 | D6.2 |  | EXEMPTION ALLOWANCE ON FED W/H |
| 176 | PC085 | D2 | D2.0 |  | MAXIMUM NUMBER OF LINES PER PAGE |
| 178 | PC090 | 9D2 | A18 |  | NUMBER OF PAY DAYS PER YEAR FOR |
| 196 | PC100 | D8 | D8.0 |  | CURRENT DATE IN USE FOR PAYROLL |
| 204 | PC105 | D2 | D2 |  | VAC PAY EARNINGS TYPE |
| 206 | PC110 | D2 | D2 |  | SICK PAY EARNINGS TYPE |
| 208 | PC120 | D5 | D5.3 |  | MINIMUM WAGE RATE |
| 213 | PC125 | A1 | A1 |  | UPDATE PAYROLL HISTORY FLAG |
| 214 | PC130 | A1 | A1 |  | W2'S TO MAGNETIC TAPE FLAG |
| 215 | PC135 | A1 | A1 |  | PRINT CHECK STUB ONLY FLAG |
| 216 | PC150 | A1 | A1 |  | PRINT CAFETERIA REPORTS |
| 217 | PC155 | A1 | A1 |  | ACCRUE VACATION FLAG |
| 218 | PC160 | D1 | D1 |  | VACATION FREQUENCY CODE |
| 219 | PC165 | D2 | D2 |  | MONTH VACATION ACCRUAL LAST RAN |
| 221 | *(filler)* | A3 | A3 |  | UNUSED SLUSH |
| 224 | PC495 | A1 | A1 |  | COMPANY STATUS |
| 225 | PC500 | A1 | A1 |  | JOB COST FLAG |
| 226 | PC505 | 99A1 | A99 |  | RATE, AMT, OR MILES DECISION TABLE |
| 325 | PC510 | A1 | A1 |  | FICA EARNINGS OPTION FLAG |
| 326 | PC515 | A8 | A8 |  | COMPANY NUMBER |
| 334 | PC520 | A30 | A30 |  | COMPANY NAME |
| 364 | PC525 | A25 | A25 |  | NAME/ADDRESS LINE 2 |
| 389 | PC530 | A25 | A25 |  | NAME/ADDRESS LINE 3 |
| 414 | PC535 | A15 | A15 |  | NAME/ADDRESS LINE 4 |
| 429 | PC540 | A2 | A2 |  | STATE CODE |
| 431 | PC545 | A9 | A9 |  | ZIP CODE |
| 440 | PC550 | A16 | A16 |  | FEDERAL ID NUMBER |
| 456 | PC565 | A1 | A1 |  | GENERAL LEDGER INTERFACE FLAG |
| 457 | PC570 | D7 | D7.2 |  | MEDICARE MAX YTD DEDUCTION |
| 464 | PC571 | D8 | D8.2 |  | MEDICARE MAXIMUM YTD TAXABLE EARNINGS |
| 472 | PC572 | D4 | D4.3 |  | MEDICARE TAX RATE |
| 476 | *(filler)* | A24 | A24 |  | SLUSH |

### (overlay 1) - COMMON, computed 126 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PC700 | 14D9 |  |  |  |

### ETTEL - COMMON, declared A9, computed 9

EARNINGS TYPE TABLE ELEMENT

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | TXFLG | 9D1 | A9 |  | THE 9 TAXABLE FLAGS FOR THIS |

## PAYCRD.FD

### PAYCR - RECORD, declared A80, computed 80

PAYROLL SYSTEM TRAN FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | ZCODE | A1 | A1 |  | CARD CODE |
| 1 | ZCLNT | D3 | D3 |  | CLIENT NUMBER |
| 4 | ZDEPT | D4 | D4 |  | DEPT NUMBER |
| 8 | ZEMPL | D5 | D5 |  | EMPLOYEE NUMBER |
| 13 | ZENDD | D8 | D8 |  | ENDING DATE OF PAY PERIOD |
| 21 | ZENDO | D8 | D8 |  | ENDING DATE OF OVERTIME |
| 29 | ZPRCK | D8 | D8 |  | DATE OF PAYROLL CHECK |
| 37 | ZPAYM | D1 | D1 |  | PAY MODE |
| 38 | ZSTCK | A6 | A6 |  | STARTING CHECK NUMBER |
| 44 | ZDEDS | D1 | D1 |  | DEDUCTION SCHEDULE |
| 45 | ZTIME | D1 | D1 |  | TIME SHEET PRINT LINES |
| 46 | *(filler)* | A34 | A34 |  | SLUSH |

### (overlay 1) - RECORD, computed 25 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | SCODE | A1 | A1 |  | CARD CODE |
| 1 | SOCLN | D3 | D3 |  | OLD CLIENT NUMBER |
| 4 | SODEP | D4 | D4 |  | OLD DEPT NUMBER |
| 8 | SOEMP | D5 | D5 |  | OLD EMPLOYEE NUMBER |
| 13 | SNCLN | D3 | D3 |  | NEW CLIENT NUMBER |
| 16 | SNDEP | D4 | D4 |  | NEW DEPT NUMBER |
| 20 | SNEMP | D5 | D5 |  | NEW EMPLOYEE NUMBER |

### (overlay 2) - RECORD, computed 76 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | NCODE | D1 | A1 |  | CARD CODE |
| 1 | NCOMP | D3 | D3 |  | COMPANY NUMBER |
| 4 | NDEPT | D4 | D4 |  | DEPARTMENT NUMBER |
| 8 | NEMPL | D5 | D5 |  | EMPLOYEE NUMBER |
| 13 | NSOCS | D9 | D9 |  | SOCIAL SECURITY NUMBER |
| 22 | NFEDX | D2 | D2 |  | NUMBER OF FEDERAL EXEMPTIONS |
| 24 | NSTAX | D2 | D2 |  | NUMBER OF STATE EXEMPTIONS |
| 26 | NCITX | D2 | D2 |  | NUMBER OF CITY EXEMPTIONS |
| 28 | NPAYM | D1 | D1 |  | PAY MODE |
| 29 | NMASK | D1 | D1 |  | MASKING FLAG |
| 30 | NPAY | D7 | D7 |  | PAY AMOUNT |
| 37 | *(filler)* | A1 | A1 |  | SLUSH |
| 38 | NOVRT | D7 | D7.4 |  | OVER TIME RATE |
| 45 | *(filler)* | A1 | A1 |  | SLUSH |
| 46 | NCOS1 | D15 | D15 |  | COST CENTER 1 |
| 61 | NCOS2 | D15 | D15 |  | COST CENTER 2 |

### (overlay 3) - RECORD, computed 83 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A13 | A13 |  | SLUSH |
| 13 | NBIRT | D8 | D8 |  | BIRTH DATE |
| 21 | NEMPD | D8 | D8 |  | EMPLOYMENT DATE |
| 29 | NFICF | D1 | D1 |  | FICA FLAG |
| 30 | NSEX | A1 | A1 |  | SEX |
| 31 | NMARS | A1 | A1 |  | MARITIAL STATUS |
| 32 | NETHN | A3 | A3 |  | ETHNIC GROUP |
| 35 | *(filler)* | A5 | A5 |  | SLUSH |
| 40 | NSORT | D4 | D4 |  | 941 SORT |
| 44 | NSTAT | D2 | D2 |  | STATE CODE |
| 46 | NCITY | D2 | D2 |  | CITY CODE |
| 48 | NEAR3 | D7 | D7.4 |  | EARNINGS 03 RATE |
| 55 | NEAR4 | D7 | D7.4 |  | EARNINGS 04 RATE |
| 62 | NEAR5 | D7 | D7.4 |  | EARNINGS 05 RATE |
| 69 | NEAR6 | D7 | D7.4 |  | EARNINGS 06 RATE |
| 76 | NEAR7 | D7 | D7.4 |  | EARNINGS 07 RATE |

### (overlay 4) - RECORD, computed 80 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A13 | A13 |  | SLUSH |
| 13 | NAME1 | A10 | A10 |  | FIRST NAME |
| 23 | NAME2 | A1 | A1 |  | MIDDLE INITIAL |
| 24 | NAME3 | A24 | A24 |  | LAST NAME |
| 48 | NADD1 | A32 | A32 |  | ADDRESS 1 |

### (overlay 5) - RECORD, computed 80 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A13 | A13 |  | SLUSH |
| 13 | NADD2 | A35 | A35 |  | ADDRESS 2 |
| 48 | NADD3 | A27 | A27 |  | ADDRESS 3 |
| 75 | NZIP | D5 | D5 |  | ZIP CODE |

### (overlay 6) - RECORD, computed 51 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | CODE1 | A1 | D1 |  | CARD CODE |
| 1 | COMP1 | D3 | D3 |  | COMPANY NUMBER |
| 4 | CDEP1 | D4 | D4 |  | DEPARTMENT NUMBER |
| 8 | CEMP1 | D5 | D5 |  | EMPLOYEE NUMBER |
| 13 | CHNG1 | D3 | D3 |  | CHANGE CODE |
| 16 | CLAST | A24 | A24 |  | LAST NAME |
| 40 | CFRST | A10 | A10 |  | FIRST NAME |
| 50 | CMIDL | A1 | A1 |  | MIDDLE INITIAL |

### (overlay 7) - RECORD, computed 51 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A16 |  |  |  |
| 16 | CADD1 | A35 | A35 |  | ADDRESS 1 |

### (overlay 8) - RECORD, computed 51 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A16 |  |  |  |
| 16 | CADD2 | A35 | A35 |  | ADDRESS 2 |

### (overlay 9) - RECORD, computed 51 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A16 |  |  |  |
| 16 | CADD3 | A30 | A30 |  | ADDRESS 3 |
| 46 | CZIP | A5 | A5 |  | ZIP CODE |

### (overlay 10) - RECORD, computed 23 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A16 |  |  |  |
| 16 | CAMNT | D7 | D7 |  | PAY RATE |

### (overlay 11) - RECORD, computed 36 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A13 |  |  |  |
| 13 | CHNG2 | A3 | A3 |  | CHANGE CODE |
| 16 | CFELD | A20 | A20 |  | NEW INFORMATION |

### (overlay 12) - RECORD, computed 35 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A16 |  |  |  |
| 16 | DTYP | D1 | D1 |  | DEDUCTION TYPE |
| 17 | DPER | D4 | D4.1 |  | DEDUCTION PERCENT |
| 21 | DAMT | D7 | D7.2 |  | DEDUCTION TYPE |
| 28 | DLMT | D7 | D7.2 |  | DEDUCTION TYPE |

### (overlay 13) - RECORD, computed 72 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | TCOD | A1 | D1 |  | CARD CODE |
| 1 | TCOM | D3 | D3 |  | COMPANY NUMBER |
| 4 | TDEP | D4 | D4 |  | DEPARTMENT NUMBER |
| 8 | TEMP | D5 | D5 |  | EMPLOYEE NUMBER |
| 13 | TDAT | D8 | D8 |  | DATE |
| 21 | TYP1 | D2 | D2 |  | TYPE # 1 |
| 23 | TUN1 | D5 | D5 |  | UNIT # 1 |
| 28 | TAM1 | D6 | D6 |  | AMOUNT # 1 |
| 34 | TYP2 | D2 | D2 |  | TYPE # 2 |
| 36 | TUN2 | D5 | D5 |  | UNIT # 2 |
| 41 | TAM2 | D6 | D6 |  | AMOUNT # 2 |
| 47 | TYP3 | D2 | D2 |  | TYPE # 3 |
| 49 | TUN3 | D5 | D5 |  | UNIT # 3 |
| 54 | TAM3 | D6 | D6 |  | AMOUNT # 3 |
| 60 | TCOS | D12 | D12 |  | COST CENTER |

### (overlay 14) - RECORD, computed 78 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | ACODE | A1 | D1 |  | CARD CODE |
| 1 | ACOMP | D3 | D3 |  | COMPANY NUMBER |
| 4 | ADEPT | D4 | D4 |  | DEPARTMENT NUMBER |
| 8 | AEMPL | D5 | D5 |  | EMPLOYEE NUMBER |
| 13 | ATYPE | D3 | D3 |  | CARD TYPE |
| 16 | ACARD | D2 | D2 |  | CARD NUMBER |
| 18 | ATIM1 | D6 | D6.2 |  | TIME # 1 |
| 24 | ATIM2 | D6 | D6.2 |  | TIME # 2 |
| 30 | ATIM3 | D6 | D6.2 |  | TIME # 3 |
| 36 | ATIM4 | D6 | D6.2 |  | TIME # 4 |
| 42 | ATIM5 | D6 | D6.2 |  | TIME # 5 |
| 48 | ATIM6 | D6 | D6.2 |  | TIME # 6 |
| 54 | ATIM7 | D6 | D6.2 |  | TIME # 7 |
| 60 | ATIM8 | D6 | D6.2 |  | TIME # 8 |
| 66 | ATIM9 | D6 | D6.2 |  | TIME # 9 |
| 72 | ATM10 | D6 | D6.2 |  | TIME # 10 |

### (overlay 15) - RECORD, computed 70 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A18 |  |  |  |
| 18 | AEAR1 | D8 | D8.2 |  | EARNING AMOUNT # 1 |
| 26 | AEAR2 | D8 | D8.2 |  | EARNING AMOUNT # 2 |
| 34 | AEAR3 | D8 | D8.2 |  | EARNING AMOUNT # 3 |
| 42 | AEAR4 | D8 | D8.2 |  | EARNING AMOUNT # 4 |
| 50 | AEAR5 | D8 | D8.2 |  | EARNING AMOUNT # 5 |
| 58 | ACOS1 | D12 | D12 |  | COST CENTER # 1 |

### (overlay 16) - RECORD, computed 70 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A18 |  |  |  |
| 18 | AEAR6 | D8 | D8.2 |  | EARNING AMOUNT # 6 |
| 26 | AEAR7 | D8 | D8.2 |  | EARNING AMOUNT # 7 |
| 34 | AEAR8 | D8 | D8.2 |  | EARNING AMOUNT # 8 |
| 42 | AEAR9 | D8 | D8.2 |  | EARNING AMOUNT # 9 |
| 50 | AER10 | D8 | D8.2 |  | EARNING AMOUNT # 10 |
| 58 | ACOS2 | D12 | D12 |  | COST CENTER # 2 |

### (overlay 17) - RECORD, computed 79 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A18 |  |  |  |
| 18 | ADED1 | D6 | D6.2 |  | DEDUCTION AMOUNT # 1 |
| 24 | ADED2 | D7 | D7.2 |  | DEDUCTION AMOUNT # 2 |
| 31 | ADED3 | D6 | D6.2 |  | DEDUCTION AMOUNT # 3 |
| 37 | ADED4 | D6 | D6.2 |  | DEDUCTION AMOUNT # 4 |
| 43 | ADED5 | D6 | D6.2 |  | DEDUCTION AMOUNT # 5 |
| 49 | ADED6 | D6 | D6.2 |  | DEDUCTION AMOUNT # 6 |
| 55 | ADED7 | D6 | D6.2 |  | DEDUCTION AMOUNT # 7 |
| 61 | ADED8 | D6 | D6.2 |  | DEDUCTION AMOUNT # 8 |
| 67 | ADED9 | D6 | D6.2 |  | DEDUCTION AMOUNT # 9 |
| 73 | ADD10 | D6 | D6.2 |  | DEDUCTION AMOUNT # 10 |

### (overlay 18) - RECORD, computed 78 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A18 |  |  |  |
| 18 | ADD11 | D6 | D6.2 |  | DEDUCTION AMOUNT # 11 |
| 24 | ADD12 | D6 | D6.2 |  | DEDUCTION AMOUNT # 12 |
| 30 | ADD13 | D6 | D6.2 |  | DEDUCTION AMOUNT # 13 |
| 36 | ADD14 | D6 | D6.2 |  | DEDUCTION AMOUNT # 14 |
| 42 | ADD15 | D6 | D6.2 |  | DEDUCTION AMOUNT # 15 |
| 48 | ADD16 | D6 | D6.2 |  | DEDUCTION AMOUNT # 16 |
| 54 | ADD17 | D6 | D6.2 |  | DEDUCTION AMOUNT # 17 |
| 60 | ADD18 | D6 | D6.2 |  | DEDUCTION AMOUNT # 18 |
| 66 | ADD19 | D6 | D6.2 |  | DEDUCTION AMOUNT # 19 |
| 72 | ADD20 | D6 | D6.2 |  | DEDUCTION AMOUNT # 20 |

### PRCTL - RECORD, computed 80 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A60 |  |  |  |
| 60 | PRDFG | D1 |  |  | DELETE FLAG |
| 61 | PRSFG | D1 |  |  | SORT FLAG |
| 62 | PRORG | D5 |  |  | ORGANIZE COUNT |
| 67 | PRREC | D5 |  |  | RECORD COUNT |
| 72 | PRMAX | D5 |  |  | MAXIMUM COUNT |
| 77 | PRDEL | D3 |  |  | DELETE COUNT |

## PAYDF.FD

### PAYDF - RECORD, declared A92, computed 92

PAYROLL DAILY FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PDJOB | D4 | D4 |  | JOB NUMBER |
| 4 | PDACT | D3 | D3 |  | ACTIVITY OR COST NUMBER |
| 7 | PDUNT | D3 | D3 |  | UNIT NUMBER |
| 10 | PDEMP | D4 | D4 |  | EMPLOYEE NUMBER |
| 14 | PDNAM | A25 | A25 |  | EMPLOYEE NAME |
| 39 | PDDAT | D8 | D8 |  | TRANSACTION DATE |
| 47 | PDCOD | A1 | A1 |  | UPDATE CODE |
| 48 | PDDOW | D2 | D2 |  | DAY OF WEEK CODE |
| 50 | PDRRT | D5 | D5.3 |  | REGULAR RATE |
| 55 | PDORT | D5 | D5.3 |  | OVERTIME RATE |
| 60 | PDRHR | D5 | D5.2 |  | REGULAR HOURS |
| 65 | PDOHR | D5 | D5.2 |  | OVERTIME HOURS |
| 70 | PDINS | A4 | A4 |  | INSURANCE CLASS CODE |
| 74 | PDCCD | A1 | A1 |  | CERTIFIED CODE |
| 75 | PDCTP | D2 | D2 |  | CERTIFIED TYPE |
| 77 | PDCDS | A15 | A15 |  | CERTIFIED DESCRIPTION |

### PDFCT - RECORD, computed 92 bytes

PAYROLL DAILY FILE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A73 |  |  |  |
| 73 | PDUPF | D1 | D1 |  | UPDATE FLAG |
| 74 | PDFOC | D5 | D5 |  | ORGANIZED COUNT |
| 79 | PDFRC | D5 | D5 |  | RECORD COUNT |
| 84 | PDFMX | D5 | D5 |  | MAXIMUM # RECORDS |
| 89 | PDFDC | D3 | D3 |  | DELETE COUNT |

## PAYMS.FD

### PAYMS - RECORD, declared A33, computed 33

PAYMS.FD (PAYMENT CODE MASTER RECORD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PYDES | A25 |  |  | PAYMENT CODE DESCRIPTION |
| 25 | PYGL | D7 |  |  | G/L NUMBER |
| 32 | PYTYP | A1 |  |  | TYPE |

## PAYWK.FD

### PAYWK - RECORD, declared A15, computed 15

PAYROLL WORK FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PWEMP | D4 | D4 |  | EMPLOYEE NUMBER |
| 4 | PWFLG | D1 | D1 |  | 1 = REGULAR  2 = O.T. |
| 5 | PWHRS | D5 | D5.2 |  | HOURS |
| 10 | PWRTE | D5 | D5.3 |  | RATE |

## PB05.FD

### PMSTR - RECORD, declared A1104, computed 1104

PB05.ISM RECORD DEFINITION

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PM005 | D4 | D4.0 |  | EMPLOYEE NUMBER (KEY FIELD) |
| 4 | PM010 | D3 | D3.0 |  | HOME DEPARTMENT NUMBER |
| 7 | PM015 | D8 | D8.0 |  | DATE OF BIRTH |
| 15 | PM020 | D8 | D8.0 |  | DATE OF EMPLOYMENT |
| 23 | PM025 | D8 | D8.0 |  | DATE OF TERMINATION |
| 31 | PM030 | 3A10 | A30 |  | COST CENTER INFO.  SEE |
| 61 | PM035 | D9 | D9.0 |  | SOCIAL SECURITY NUMBER |
| 70 | PM040 | D1 | D1.0 |  | PAYMENT MODE |
| 71 | PM045 | D8 | D8.0 |  | LAST TRX DATE |
| 79 | PM050 | D8 | D8.0 |  | DATE OF LAST SALARY CHANGE |
| 87 | PM055 | D2 | D2.0 |  | NUMBER OF FEDERAL EXEMPTIONS |
| 89 | PM060 | D2 | D2.0 |  | NUMBER OF STATE EXEMPTIONS |
| 91 | PM065 | D2 | D2.0 |  | ANNUAL VACATION MONTH |
| 93 | PM070 | D5 | D5.3 |  | EARNINGS 1 PAY RATE |
| 98 | PM075 | D5 | D5.3 |  | EARNINGS 2 PAY RATE |
| 103 | PM080 | D7 | D7.2 |  | BASE PAY |
| 110 | PM085 | D7 | D7.2 |  | ADDITIONAL FED W/H |
| 117 | PM090 | D7 | D7.2 |  | ADDITIONAL STATE W/H |
| 124 | PM095 | D6 | D6.2 |  | MTD 401K SUTA |
| 130 | PM100 | D1 | D1 |  | VACATION TYPE CODE |
| 131 | PM110 | 5A26 | A130 |  | DEDUCTION TABLE WITH LIMITS. |
| 261 | PM115 | 15A18 | A270 |  | DEDUCTION TABLE WITHOUT LIMITS. |
| 531 | PM117 | D8 | D8.2 |  | QTD GROSS EARNINGS FOR ALL TYPES |
| 539 | PM120 | 14D8 | A112 |  | YTD GROSS EARNINGS (D8.2) FOR EACH |
| 651 | PM123 | D8 | D8.2 |  | SOCIAL SECURITY QTD DEDUCTIONS |
| 659 | PM125 | D8 | D8.2 |  | SOCIAL SECURITY YTD DEDUCTIONS |
| 667 | PM128 | D8 | D8.2 |  | FED W/H QTD DEDUCTIONS |
| 675 | PM130 | D8 | D8.2 |  | FED W/H YTD DEDUCTIONS |
| 683 | PM133 | D8 | D8.2 |  | STATE W/H QTD DEDUCTIONS |
| 691 | PM135 | D8 | D8.2 |  | STATE W/H YTD DEDUCTIONS |
| 699 | PM138 | D7 | D7.2 |  | QTD 401K SUTA |
| 706 | *(filler)* | A1 | A1 |  | SLUSH |
| 707 | PM140 | D6 | D6.2 |  | MTD 401K FUTA |
| 713 | PM141 | D7 | D7.2 |  | QTD 401K FUTA |
| 720 | PM143 | D5 | D5.2 |  | MTD 125 FUTA |
| 725 | PM145 | D6 | D6.2 |  | QTD 125 FUTA |
| 731 | PM150 | D8 | D8.2 |  | SOCIAL SECURITY QTD TAXABLE EARNINGS |
| 739 | PM155 | D8 | D8.2 |  | SOCIAL SECURITY YTD TAXABLE EARNINGS |
| 747 | PM158 | D8 | D8.2 |  | FED W/H QTD TAXABLE EARNINGS |
| 755 | PM160 | D8 | D8.2 |  | FED W/H YTD TAXABLE EARNINGS |
| 763 | PM163 | D8 | D8.2 |  | STATE W/H QTD TAXABLE EARNINGS |
| 771 | PM165 | D8 | D8.2 |  | STATE W/H YTD TAXABLE EARNINGS |
| 779 | PM168 | D5 | D5.2 |  | MTD 125 SUTA |
| 784 | PM170 | D6 | D6.2 |  | QTD 125 SUTA |
| 790 | PM171 | D7 | D7.2 |  | MTD 401K |
| 797 | PM175 | D7 | D7.2 |  | MTD EARNINGS |
| 804 | PM180 | D7 | D7.2 |  | MTD TIPS |
| 811 | PM185 | D5 | D5.2 |  | ACCRUED VACATION HOURS |
| 816 | PM190 | D5 | D5.2 |  | ACCRUED SICK HOURS |
| 821 | PM192 | D7 | D7.2 |  | TIPS QTD |
| 828 | PM195 | D3 | D3.1 |  | FED W/H PERCENT |
| 831 | PM205 | D2 | D2.0 |  | STATE TAX CODE |
| 833 | PM210 | D2 | D2 |  | SLUSH |
| 835 | PM215 | D6 | D6.2 |  | REGULAR HOURS YTD |
| 841 | PM220 | D6 | D6.2 |  | OVERTIME HOURS YTD |
| 847 | PM230 | D2 | D2 |  | CERTIFIED TYPE |
| 849 | *(filler)* | A2 | A2 |  | SLUSH |
| 851 | PM505 | A25 | A25 |  | NAME/ADDRESS LINE 1 |
| 876 | PM510 | A25 | A25 |  | NAME/ADDRESS LINE 2 |
| 901 | PM515 | A25 | A25 |  | NAME/ADDRESS LINE 3 |
| 926 | PM520 | A15 | A15 |  | CITY |
| 941 | PM525 | A2 | A2 |  | STATE CODE |
| 943 | PM530 | A9 | A9 |  | ZIP CODE |
| 952 | PM535 | A15 | A15 |  | SHORT NAME |
| 967 | PM540 | A3 | A3 |  | ETHNIC GROUP |
| 970 | PM545 | A1 | A1 |  | SALARY CODE |
| 971 | PM550 | A1 | A1 |  | MARITAL STATUS |
| 972 | PM555 | A1 | A1 |  | SEX |
| 973 | PM560 | A1 | A1 |  | EMPLOYEE STATUS |
| 974 | PM565 | A1 | A1 |  | FICA FLAG |
| 975 | PM570 | A1 | A1 |  | PENSION FLAG |
| 976 | PM580 | D8 | D8.2 |  | MEDICARE QTD TAXABLE |
| 984 | PM585 | D8 | D8.2 |  | MEDICARE YTD TAXABLE |
| 992 | PM590 | D8 | D8.2 |  | MEDICARE QTD DEDUCTIONS |
| 1000 | PM595 | D8 | D8.2 |  | MEDICARE YTD DEDUCTIONS |
| 1008 | PM600 | D7 | D7.2 |  | MTD 125 (CAFETERIA) |
| 1015 | PM605 | D6 | D6.2 |  | TOTAL HOURS MTD |
| 1021 | PM610 | D6 | D6.2 |  | TOTAL HOURS YTD |
| 1027 | PM615 | A1 | A1 |  | ADVANCE EIC FLAG |
| 1028 | PM620 | D6 | D6.2 |  | ADV EIC QTD |
| 1034 | PM625 | D6 | D6.2 |  | ADV EIC YTD |
| 1040 | *(filler)* | A64 |  |  | SLUSH |

### COSTI - RECORD, declared A10, computed 10

COST CENTER INFORMATION

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PCPCT | D3 |  |  | PERCENT OF SALARY ALLOCATED TO |
| 3 | PCGLA | D7 | D7.0 |  | GENERAL LEDGER ACCOUNT NUMBER |

### DEDTB - RECORD, declared A26, computed 26

DEDUCTION TABLE ELEMENT

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PDTYP | D2 | D2.0 |  | TYPE CODE |
| 2 | PDFRQ | D1 | D1.0 |  | FREQUENCY OF DEDUCTION |
| 3 | PDAMT | D7 | D7.2 |  | AMOUNT OF DEDUCTION |
| 10 | PDYTD | D8 | D8.2 |  | YTD ACCUMULATION |
| 18 | PDLMT | D8 | D8.2 |  | TOP LIMIT OF DEDUCTION |

## PB05.FDC

### PMSTR - COMMON, declared A1104, computed 1104

PB05.ISM RECORD DEFINITION

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PM005 | D4 | D4.0 |  | EMPLOYEE NUMBER (KEY FIELD) |
| 4 | PM010 | D3 | D3.0 |  | HOME DEPARTMENT NUMBER |
| 7 | PM015 | D8 | D8.0 |  | DATE OF BIRTH |
| 15 | PM020 | D8 | D8.0 |  | DATE OF EMPLOYMENT |
| 23 | PM025 | D8 | D8.0 |  | DATE OF TERMINATION |
| 31 | PM030 | 3A10 | A30 |  | COST CENTER INFO.  SEE |
| 61 | PM035 | D9 | D9.0 |  | SOCIAL SECURITY NUMBER |
| 70 | PM040 | D1 | D1.0 |  | PAYMENT MODE |
| 71 | PM045 | D8 | D8.0 |  | LAST TRX DATE |
| 79 | PM050 | D8 | D8.0 |  | DATE OF LAST SALARY CHANGE |
| 87 | PM055 | D2 | D2.0 |  | NUMBER OF FEDERAL EXEMPTIONS |
| 89 | PM060 | D2 | D2.0 |  | NUMBER OF STATE EXEMPTIONS |
| 91 | PM065 | D2 | D2.0 |  | ANNUAL VACATION MONTH |
| 93 | PM070 | D5 | D5.3 |  | EARNINGS 1 PAY RATE |
| 98 | PM075 | D5 | D5.3 |  | EARNINGS 2 PAY RATE |
| 103 | PM080 | D7 | D7.2 |  | BASE PAY |
| 110 | PM085 | D7 | D7.2 |  | ADDITIONAL FED W/H |
| 117 | PM090 | D7 | D7.2 |  | ADDITIONAL STATE W/H |
| 124 | PM095 | D6 | D6.2 |  | MTD 401K SUTA |
| 130 | PM100 | D1 | D1 |  | VACATION TYPE CODE |
| 131 | PM110 | 5A26 | A130 |  | DEDUCTION TABLE WITH LIMITS. |
| 261 | PM115 | 15A18 | A270 |  | DEDUCTION TABLE WITHOUT LIMITS. |
| 531 | PM117 | D8 | D8.2 |  | QTD GROSS EARNINGS FOR ALL TYPES |
| 539 | PM120 | 14D8 | A112 |  | YTD GROSS EARNINGS (D8.2) FOR EACH |
| 651 | PM123 | D8 | D8.2 |  | SOCIAL SECURITY QTD DEDUCTIONS |
| 659 | PM125 | D8 | D8.2 |  | SOCIAL SECURITY YTD DEDUCTIONS |
| 667 | PM128 | D8 | D8.2 |  | FED W/H QTD DEDUCTIONS |
| 675 | PM130 | D8 | D8.2 |  | FED W/H YTD DEDUCTIONS |
| 683 | PM133 | D8 | D8.2 |  | STATE W/H QTD DEDUCTIONS |
| 691 | PM135 | D8 | D8.2 |  | STATE W/H YTD DEDUCTIONS |
| 699 | PM138 | D7 | D7.2 |  | QTD 401K SUTA |
| 706 | *(filler)* | A1 | A1 |  | SLUSH |
| 707 | PM140 | D6 | D6.2 |  | MTD 401K FUTA |
| 713 | PM141 | D7 | D7.2 |  | QTD 401K FUTA |
| 720 | PM143 | D5 | D5.2 |  | MTD 125 FUTA |
| 725 | PM145 | D6 | D6.2 |  | QTD 125 FUTA |
| 731 | PM150 | D8 | D8.2 |  | SOCIAL SECURITY QTD TAXABLE EARNINGS |
| 739 | PM155 | D8 | D8.2 |  | SOCIAL SECURITY YTD TAXABLE EARNINGS |
| 747 | PM158 | D8 | D8.2 |  | FED W/H QTD TAXABLE EARNINGS |
| 755 | PM160 | D8 | D8.2 |  | FED W/H YTD TAXABLE EARNINGS |
| 763 | PM163 | D8 | D8.2 |  | STATE W/H QTD TAXABLE EARNINGS |
| 771 | PM165 | D8 | D8.2 |  | STATE W/H YTD TAXABLE EARNINGS |
| 779 | PM168 | D5 | D5.2 |  | MTD 125 SUTA |
| 784 | PM170 | D6 | D6.2 |  | QTD 125 SUTA |
| 790 | PM171 | D7 | D7.2 |  | MTD 401K |
| 797 | PM175 | D7 | D7.2 |  | MTD EARNINGS |
| 804 | PM180 | D7 | D7.2 |  | MTD TIPS |
| 811 | PM185 | D5 | D5.2 |  | ACCRUED VACATION HOURS |
| 816 | PM190 | D5 | D5.2 |  | ACCRUED SICK HOURS |
| 821 | PM192 | D7 | D7.2 |  | TIPS QTD |
| 828 | PM195 | D3 | D3.1 |  | FED W/H PERCENT |
| 831 | PM205 | D2 | D2.0 |  | STATE TAX CODE |
| 833 | PM210 | D2 | D2 |  | SLUSH |
| 835 | PM215 | D6 | D6.2 |  | REGULAR HOURS YTD |
| 841 | PM220 | D6 | D6.2 |  | OVERTIME HOURS YTD |
| 847 | PM230 | D2 | D2 |  | CERTIFIED TYPE |
| 849 | *(filler)* | A2 | A2 |  | SLUSH |
| 851 | PM505 | A25 | A25 |  | NAME/ADDRESS LINE 1 |
| 876 | PM510 | A25 | A25 |  | NAME/ADDRESS LINE 2 |
| 901 | PM515 | A25 | A25 |  | NAME/ADDRESS LINE 3 |
| 926 | PM520 | A15 | A15 |  | CITY |
| 941 | PM525 | A2 | A2 |  | STATE CODE |
| 943 | PM530 | A9 | A9 |  | ZIP CODE |
| 952 | PM535 | A15 | A15 |  | SHORT NAME |
| 967 | PM540 | A3 | A3 |  | ETHNIC GROUP |
| 970 | PM545 | A1 | A1 |  | SALARY CODE |
| 971 | PM550 | A1 | A1 |  | MARITAL STATUS |
| 972 | PM555 | A1 | A1 |  | SEX |
| 973 | PM560 | A1 | A1 |  | EMPLOYEE STATUS |
| 974 | PM565 | A1 | A1 |  | FICA FLAG |
| 975 | PM570 | A1 | A1 |  | PENSION FLAG |
| 976 | PM580 | D8 | D8.2 |  | MEDICARE QTD TAXABLE |
| 984 | PM585 | D8 | D8.2 |  | MEDICARE YTD TAXABLE |
| 992 | PM590 | D8 | D8.2 |  | MEDICARE QTD DEDUCTIONS |
| 1000 | PM595 | D8 | D8.2 |  | MEDICARE YTD DEDUCTIONS |
| 1008 | PM600 | D7 | D7.2 |  | MTD 125 (CAFETERIA) |
| 1015 | PM605 | D6 | D6.2 |  | TOTAL HOURS MTD |
| 1021 | PM610 | D6 | D6.2 |  | TOTAL HOURS YTD |
| 1027 | PM615 | A1 | A1 |  | ADVANCE EIC FLAG |
| 1028 | PM620 | D6 | D6.2 |  | ADV EIC QTD |
| 1034 | PM625 | D6 | D6.2 |  | ADV EIC YTD |
| 1040 | *(filler)* | A64 |  |  | SLUSH |

### COSTI - COMMON, declared A10, computed 10

COST CENTER INFORMATION

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PCPCT | D3 |  |  | PERCENT OF SALARY ALLOCATED TO |
| 3 | PCGLA | D7 | D7.0 |  | GENERAL LEDGER ACCOUNT NUMBER |

### DEDTB - COMMON, declared A26, computed 26

DEDUCTION TABLE ELEMENT

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PDTYP | D2 | D2.0 |  | TYPE CODE |
| 2 | PDFRQ | D1 | D1.0 |  | FREQUENCY OF DEDUCTION |
| 3 | PDAMT | D7 | D7.2 |  | AMOUNT OF DEDUCTION |
| 10 | PDYTD | D8 | D8.2 |  | YTD ACCUMULATION |
| 18 | PDLMT | D8 | D8.2 |  | TOP LIMIT OF DEDUCTION |

## PB10.FD

### PADLG - RECORD, declared A29, computed 29

PB10.DDF RECORD DEFINITION (ADD/DELETE LOG)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PAD05 | A1 |  |  | = 'A' FOR ADD, = 'D' FOR DELETE |
| 1 | PAD10 | D4 |  |  | EMPLOYEE NUMBER |
| 5 | PAD12 | D8 |  |  | DATE ADDITION OR DELETION WAS MADE |
| 13 | PAD15 | A15 |  |  | SHORT NAME |
| 28 | PAD20 | A1 |  |  | SALARY CODE |

### CTL10,X - RECORD, computed 29 bytes

CONTROL RECORD FOR PB10.DDF

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A18 |  |  |  |
| 18 | LCK10 | A1 |  |  | LOCK FLAG |
| 19 | REC10 | D5 |  |  | RECORD COUNT |
| 24 | MAX10 | D5 |  |  | MAXIMUM COUNT |

## PB15.FD

### PCHLG - RECORD, declared A97, computed 97

PB15.DDF RECORD DEFINITION (CHANGE LOG)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PCH05 | D4 |  |  | EMPLOYEE NUMBER |
| 4 | PCH07 | D8 |  |  | DATE THAT THE CHANGE WAS MADE |
| 12 | PCH10 | A15 |  |  | SHORT NAME |
| 27 | PCH15 | A20 |  |  | FIELD THAT WAS CHANGED |
| 47 | PCH20 | A25 |  |  | OLD INFORMATION |
| 72 | PCH25 | A25 |  |  | NEW INFORMATION |

### CTL15,X - RECORD, computed 97 bytes

CONTROL RECORD FOR PB15.DDF

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A86 |  |  |  |
| 86 | LCK15 | A1 |  |  | LOCK FLAG |
| 87 | REC15 | D5 |  |  | RECORD COUNT |
| 92 | MAX15 | D5 |  |  | MAXIMUM COUNT |

## PC05.FD

### PMIDX - RECORD, computed 26 bytes

PC05.DDF RECORD DEFINITION

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PIX05 | A15 |  |  | SHORT NAME |
| 15 | PIX10 | D4 |  |  | EMPLOYEE NUMBER |
| 19 | PIX15 | D7 |  |  | RECORD NUMBER IN PB05.ISM MASTER FILE |

## PD05.FD

### PTRAX - RECORD, declared A989, computed 989

PD05.ISM RECORD DEFINITION

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PT005 | D4 | D4.0 |  | EMPLOYEE NUMBER (KEY FIELD) |
| 4 | PT010 | 12A36 | A432 |  | THE 12 EARNINGS TYPES. |
| 436 | PT015 | D8 | D8.2 |  | GROSS PAY |
| 444 | PT020 | D8 | D8.2 |  | NET PAY |
| 452 | PT025 | D6 | D6.0 |  | CHECK NUMBER |
| 458 | PT030 | D8 | D8.2 |  | SOC SEC TAX DEDUCTED |
| 466 | PT035 | D8 | D8.2 |  | FED W/H TAX DEDUCTED |
| 474 | PT040 | D8 | D8.2 |  | STATE W/H TAX DEDUCTED |
| 482 | PT045 | D8 | D8.2 |  | MEDICARE TAX DEDUCTED |
| 490 | PT050 | D8 |  |  | SLUSH |
| 498 | PT055 | D8 | D8.2 |  | SOC SEC TAXABLE EARNINGS |
| 506 | PT060 | D8 | D8.2 |  | FED W/H TAXABLE EARNINGS |
| 514 | PT065 | D8 | D8.2 |  | STATE W/H TAXABLE EARNINGS |
| 522 | PT070 | D8 | D8.2 |  | MEDICARE TAXABLE EARNINGS |
| 530 | PT075 | D8 | D8.2 |  | ADVANCE EIC PAYMENT |
| 538 | PT080 | 20D2 | A40 |  | THE 20 DEDUCTION CODES (D2.0) |
| 578 | PT085 | 20D7 | A140 |  | THE 20 DEDUCTION AMOUNTS (D7.2) |
| 718 | PT100 | D5 | D5.2 |  | VACATION HOURS ACCRUED |
| 723 | PT105 | D5 | D5.2 |  | SICK HOURS ACCRUED |
| 728 | PT110 | 14D8 | A112 |  | GROSS EARNINGS (D7.2) FOR EACH OF |
| 840 | PT115 | D8 | D8.0 |  | DATE OF PAYCHECK |
| 848 | PT120 | 3A10 | A30 |  | COST CENTER INFO.  SEE |
| 878 | PT125 | D8 | D8.0 |  | DATE OF TRANSACTION |
| 886 | PT130 | D5 | D5.2 |  | REGULAR HOURS WORKED |
| 891 | PT135 | D5 | D5.2 |  | OVERTIME HOURS WORKED |
| 896 | PT140 | D2 | D2 |  | NBR OF EXEMPTIONS |
| 898 | PT505 | A1 | A1 |  | SALARY CODE |
| 899 | PT510 | A15 | A15 |  | SHORT NAME |
| 914 | PT530 | D5 | D5.2 |  | TOTAL HOURS WORKED |
| 919 | PT610 | 14D5 | A70 |  | HOURS (D5.2) FOR EACH OF |

### ERNTY - RECORD, declared A35, computed 36  **MISMATCH**

EARNINGS TYPE ELEMENT

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PETYG | D2 | D2.0 |  | GENERAL EARNINGS TYPE |
| 2 | PETYS | D2 | D2.0 |  | SPECIFIC EARNINGS TYPE |
| 4 | PEHRS | D5 |  |  | HOURS(D5.2),  OR MILES(D5.1)		D5.X |
| 9 | PEROA | D8 |  |  | RATE(D7.3), AMT(D7.2), MILAGE(D7.7)   D7.X |
| 17 | PEGLA | D7 | D7.0 |  | GENERAL LEDGER ACCOUNT NUMBER |
| 24 | PEJNO | D7 | D7.0 |  | JOB NUMBER |
| 31 | PEJRT | D5 | D5.2 |  | JOB COST RATE |

## PD05.FDC

### PTRAX - COMMON, declared A989, computed 989

PD05.ISM RECORD DEFINITION

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PT005 | D4 | D4.0 |  | EMPLOYEE NUMBER (KEY FIELD) |
| 4 | PT010 | 12A36 | A432 |  | THE 12 EARNINGS TYPES. |
| 436 | PT015 | D8 | D8.2 |  | GROSS PAY |
| 444 | PT020 | D8 | D8.2 |  | NET PAY |
| 452 | PT025 | D6 | D6.0 |  | CHECK NUMBER |
| 458 | PT030 | D8 | D8.2 |  | SOC SEC TAX DEDUCTED |
| 466 | PT035 | D8 | D8.2 |  | FED W/H TAX DEDUCTED |
| 474 | PT040 | D8 | D8.2 |  | STATE W/H TAX DEDUCTED |
| 482 | PT045 | D8 | D8.2 |  | MEDICARE TAX DEDUCTED |
| 490 | PT050 | D8 |  |  | SLUSH |
| 498 | PT055 | D8 | D8.2 |  | SOC SEC TAXABLE EARNINGS |
| 506 | PT060 | D8 | D8.2 |  | FED W/H TAXABLE EARNINGS |
| 514 | PT065 | D8 | D8.2 |  | STATE W/H TAXABLE EARNINGS |
| 522 | PT070 | D8 | D8.2 |  | MEDICARE TAXABLE EARNINGS |
| 530 | PT075 | D8 | D8.2 |  | ADVANCE EIC PAYMENT |
| 538 | PT080 | 20D2 | A40 |  | THE 20 DEDUCTION CODES (D2.0) |
| 578 | PT085 | 20D7 | A140 |  | THE 20 DEDUCTION AMOUNTS (D7.2) |
| 718 | PT100 | D5 | D5.2 |  | VACATION HOURS ACCRUED |
| 723 | PT105 | D5 | D5.2 |  | SICK HOURS ACCRUED |
| 728 | PT110 | 14D8 | A112 |  | GROSS EARNINGS (D7.2) FOR EACH OF |
| 840 | PT115 | D8 | D8.0 |  | DATE OF PAYCHECK |
| 848 | PT120 | 3A10 | A30 |  | COST CENTER INFO.  SEE |
| 878 | PT125 | D8 | D8.0 |  | DATE OF TRANSACTION |
| 886 | PT130 | D5 | D5.2 |  | REGULAR HOURS WORKED |
| 891 | PT135 | D5 | D5.2 |  | OVERTIME HOURS WORKED |
| 896 | PT140 | D2 | D2 |  | NBR OF EXEMPTIONS |
| 898 | PT505 | A1 | A1 |  | SALARY CODE |
| 899 | PT510 | A15 | A15 |  | SHORT NAME |
| 914 | PT530 | D5 | D5.2 |  | TOTAL HOURS WORKED |
| 919 | PT610 | 14D5 | A70 |  | HOURS (D5.2) FOR EACH OF |

### ERNTY - COMMON, declared A35, computed 36  **MISMATCH**

EARNINGS TYPE ELEMENT

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PETYG | D2 | D2.0 |  | GENERAL EARNINGS TYPE |
| 2 | PETYS | D2 | D2.0 |  | SPECIFIC EARNINGS TYPE |
| 4 | PEHRS | D5 |  |  | HOURS(D5.2),  OR MILES(D5.1)		D5.X |
| 9 | PEROA | D8 |  |  | RATE(D7.3), AMT(D7.2), MILAGE(D7.7)   D7.X |
| 17 | PEGLA | D7 | D7.0 |  | GENERAL LEDGER ACCOUNT NUMBER |
| 24 | PEJNO | D7 | D7.0 |  | JOB NUMBER |
| 31 | PEJRT | D5 | D5.2 |  | JOB COST RATE |

## PE08.FD

### PRPTS - RECORD, declared A37, computed 37

PE08.DDF RECORD DEFINITION

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PR005 | D2 | D2.0 |  | REPORTS CODE |
| 2 | PR010 | D4 | D4.0 |  | EMPLOYEE NUMBER |
| 6 | PR015 | D2 | D2.0 |  | DEDUCTION TYPE |
| 8 | PR020 | D7 | D7.2 |  | DEDUCTION AMT WHICH WAS TOO BIG |
| 15 | PR025 | D7 | D7.2 |  | DEDUCTION AMT ACTUALLY TAKEN |
| 22 | PR505 | A15 | A15 |  | SHORT NAME |

## PE35.FD

### PBANK - RECORD, computed 72 bytes

A72

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PB005 | D6 |  |  | CHECK NUMBER |
| 6 | PB010 | A25 |  |  | NAME |
| 31 | PB015 | D10 |  |  | CHECK AMOUNT |
| 41 | PB020 | D8 |  |  | CHECK DATE |
| 49 | PB025 | A18 |  |  | INVOICE NUMBER |
| 67 | PB030 | D1 |  |  | DELETE FLAG	0 = UNCLEARED |
| 68 | *(filler)* | A4 |  |  | SLUSH |

### CNTRL - RECORD, computed 72 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A62 |  |  |  |
| 62 | RECCNT | D5 |  |  | RECORD COUNT |
| 67 | MAXCNT | D5 |  |  | MAX COUNT |

## PE35.FDC

### PBANK - COMMON, computed 72 bytes

A72

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PB005 | D6 |  |  | CHECK NUMBER |
| 6 | PB010 | A25 |  |  | NAME |
| 31 | PB015 | D10 |  |  | CHECK AMOUNT |
| 41 | PB020 | D8 |  |  | CHECK DATE |
| 49 | PB025 | A18 |  |  | INVOICE NUMBER |
| 67 | PB030 | D1 |  |  | DELETE FLAG |
| 68 | *(filler)* | A4 |  |  | SLUSH |

### CNTRL - COMMON, computed 72 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A62 |  |  |  |
| 62 | RECCT | D5 |  |  | RECORD COUNT |
| 67 | MXCNT | D5 |  |  | MAX COUNT |

## PF20.FD

### PAWRK - RECORD, computed 404 bytes

PAYROLL COST ANALYSIS WORK RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PA005 | D7 |  |  | G/L ACCOUNT NUMBER |
| 7 | PA010 | D4 |  |  | EMPLOYEE NUMBER |
| 11 | PA015 | 15D8 |  |  | THE 14 TYPES OF EARNINGS AND THE GRAND TOTAL |
| 131 | PA020 | 26D8 |  |  | THE 25 DEDUCTIONS AND THE GRAND TOTAL |
| 339 | PA025 | 25D2 |  |  | THE 25 DEDUCTION CODES |
| 389 | PA505 | A15 |  |  | SHORT NAME |

## PF40.FD

### PHIST - RECORD, declared A400, computed 400

PAYROLL HISTORY FILE (PF40.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PH005 | D4 | D4 |  | EMPLOYEE NUMBER |
| 4 | PH010 | D6 | D6 |  | CHECK NUMBER |
| 10 | PH015 | D8 | D8.2 |  | FICA TAX DEDUCTED |
| 18 | PH020 | D8 | D8.2 |  | FED W/H TAX DEDUCTED |
| 26 | PH025 | D8 | D8.2 |  | STATE W/H TAX DEDUCTED |
| 34 | PH030 | D8 | D8.2 |  | CITY W/H TAX DEDUCTED |
| 42 | PH035 | D8 | D8.2 |  | STATE INSURANCE DEDUCTED |
| 50 | PH040 | D8 | D8.2 |  | TOTAL OTHER DEDUCTIONS |
| 58 | PH045 | 14D8 | D112 |  | GROSS EARNINGS FOR EACH EARN TYPE |
| 170 | PH047 | 14D5 | D70 |  | HOURS FOR EACH EARNING TYPE |
| 240 | PH050 | D8 | D8 |  | DATE OF PAYCHECK |
| 248 | PH055 | D5 | D5.2 |  | REGULAR HOURS WORKED |
| 253 | PH060 | D5 | D5.2 |  | OVERTIME HOURS WORKED |
| 258 | PH065 | D1 |  |  | 0 = REGULAR TRX  1 = MANUAL TRX (*) |
| 259 | PH070 | A15 | A15 |  | EMPLOYEE SHORT NAME |
| 274 | PH075 | D9 | D9 |  | SOCIAL SECURITY NUMBER |
| 283 | PH080 | D8 | D8 |  | DATE OF EMPLOYMENT |
| 291 | PH085 | D8 | D8 |  | DATE OF TERMINATION |
| 299 | PH095 | 14D2 | D28 |  | GENERAL EARNINGS TYPE |
| 327 | PH100 | D8 | D8 |  | ADV EIC PAYMENT |
| 335 | *(filler)* | A65 | A65 |  | SLUSH |

### PHCTL - RECORD, computed 400 bytes

CONTROL RECORD DEFINITION

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A390 |  |  |  |
| 390 | PHREC | D5 |  |  | RECORD COUNT |
| 395 | PHMAX | D5 |  |  | MAXIMUM COUNT |

## PF42.FD

### PEYTD - RECORD, computed 54 bytes

EMPLOYEE YTD INFO FOR EACH COST CENTER

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PY005 | D4 |  |  | EMPLOYEE NUMBER |
| 4 | PY010 | D7 |  |  | COST CENTER |
| 11 | PY015 | D6 |  |  | REGULAR HOURS |
| 17 | PY020 | D8 |  |  | REGULAR DOLLARS |
| 25 | PY025 | D6 |  |  | OVT HOURS |
| 31 | PY030 | D8 |  |  | OVT DOLLARS |
| 39 | PY505 | A15 |  |  | SHORT NAME |

## PF44.FD

### PZYTD - RECORD, computed 54 bytes

EMPLOYEE YTD INFO FOR EACH COST CENTER

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PZ005 | D4 |  |  | EMPLOYEE NUMBER |
| 4 | PZ010 | D7 |  |  | COST CENTER |
| 11 | PZ015 | D6 |  |  | REGULAR HOURS |
| 17 | PZ020 | D8 |  |  | REGULAR DOLLARS |
| 25 | PZ025 | D6 |  |  | OVT HOURS |
| 31 | PZ030 | D8 |  |  | OVT DOLLARS |
| 39 | PZ505 | A15 |  |  | SHORT NAME |

## PF50.FD

### PJWRK - RECORD, declared A47, computed 47

JOB COST WORK FILE RECORD DEFINITION (PF50.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PJ005 | D7 | D7 |  | JOB NUMBER |
| 7 | PJ010 | D4 | D4 |  | EMPLOYEE NUMBER |
| 11 | PJ015 | D5 | D5.2 |  | JOB COST RATE |
| 16 | PJ020 | D4 | D4.2 |  | REGULAR HOURS |
| 20 | PJ025 | D4 | D4.2 |  | O.T. HOURS |
| 24 | PJ030 | D8 | D8.2 |  | JOB COST AMOUNT |
| 32 | PJ035 | A15 | A15 |  | SHORT NAME |

## PF83.FD

### PGPWK - RECORD, declared A29, computed 29

GROSS PAY BY STATE WORK FILE (PF83.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PGP05 | D4 | D4 |  | EMPLOYEE NUMBER |
| 4 | PGP10 | A15 | A15 |  | SHORT NAME |
| 19 | PGP15 | D8 | D8 |  | GROSS PAY |
| 27 | PGP20 | D2 | D2 |  | STATE CODE |

## PH10.FD

### PGOVT - RECORD, declared A200, computed 200

PH10.DDF RECORD DEFINITION

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PG005 | D8 | D8.2 |  | STATE'S TAXABLE WAGE LIMIT |
| 8 | *(filler)* | A54 |  |  |  |
| 62 | PG505 | A30 | A30 |  | NAME/ADDRESS LINE ONE |
| 92 | PG510 | A25 | A25 |  | NAME/ADDRESS LINE TWO |
| 117 | PG515 | A25 | A25 |  | NAME/ADDRESS LINE THREE |
| 142 | PG520 | A15 | A15 |  | NAME/ADDRESS LINE FOUR |
| 157 | PG525 | A2 | A2 |  | STATE CODE |
| 159 | PG530 | A9 | A9 |  | ZIP CODE |
| 168 | PG535 | A16 | A16 |  | STATE ID NBR |
| 184 | PG540 | A16 | A16 |  | NAME OF STATE |

## PH11.FD

### PFOVT - RECORD, declared A200, computed 200

PH11.DDF RECORD DEFINITION

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PF005 | D8 | D8.2 |  | FED'S TAXABLE WAGE LIMIT |
| 8 | *(filler)* | A192 | A192 |  | SLUSH |

## PHVIX.FD

### PHVIX - RECORD, declared A14, computed 14

TEMP PURCHASE ORDER HEADER VENDOR INDEX (PHVIX.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | VHVND | D4 | D4 |  | VENDOR NUMBER |
| 4 | VHNUM | D5 | D5 |  | PURCHASE ORDER NUMBER |
| 9 | VHRNO | D5 | D5 |  | RECORD NUMBER |

### (overlay 1) - RECORD, computed 4 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | VHVNA | A4 |  |  | ALPHA VENDOR NUMBER |

## PK30.FD

### PDECO - RECORD, computed 0 bytes

DEDUCTION PERCENTAGE/AMOUNT CODE RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|

## PK30.FDC

### PDECO - COMMON, computed 0 bytes

DEDUCTION PERCENTAGE/AMOUNT CODE RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|

## PK500.FDC

### PK500 - COMMON, declared A118, computed 118

DEDUCTION TAXABLE CODE RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PK010 | A1 |  |  | SOC SEC EARNINGS N OR G |
| 1 | PK020 | A1 |  |  | F/W EARNINGS N OR G |
| 2 | PK030 | 99A1 |  |  | 99 STATE TAXABLE CODES N OR G |
| 101 | PK040 | A1 |  |  | FUTA N OR G |
| 102 | PK050 | A1 |  |  | SUTA N OR G |
| 103 | PK060 | A1 |  |  | 401K DEDUCTION Y OR N |
| 104 | PK070 | A1 |  |  | CAFETERIA DEDUCTION Y OR N |
| 105 | PK080 | A1 |  |  | DEPENDENT CHILD CARE DEDUCTION Y OR N |
| 106 | PK090 | A1 |  |  | MEDICARE EARNINGS N OR G |
| 107 | PK065 | A1 |  |  | 401K CODE (D,E,F,G,H) |
| 108 | *(filler)* | A10 |  |  | SLUSH |

## PLVIX.FD

### PLVIX - RECORD, declared A21, computed 21

TEMP PURCHASE ORDER LINE VENDOR INDEX (PLVIX.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | VLVND | D4 | D4 |  | VENDOR NUMBER |
| 4 | VLNUM | D5 | D5 |  | PURCHASE ORDER NUMBER |
| 9 | VLITM | D7 | D7 |  | LINE ITEM NUMBER |
| 16 | VLRNO | D5 | D5 |  | RECORD NUMBER |

### (overlay 1) - RECORD, computed 4 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | VLVNA | A4 |  |  | ALPHA VENDOR NUMBER |

## PM10.FD

### PMAG - RECORD, declared A232, computed 232

PM10.DDF RECORD DEF MAG TAPE FILE (PM10.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | MG005 | D9 |  |  | SOC SEC # |
| 9 | MG010 | A27 |  |  | NAME |
| 36 | MG015 | A40 |  |  | ADDRESS |
| 76 | MG020 | A25 |  |  | CITY |
| 101 | MG025 | A10 |  |  | STATE |
| 111 | MG030 | D5 |  |  | ZIP |
| 116 | MG035 | D7 |  |  | YTD SOC SEC WAGES |
| 123 | MG040 | D7 |  |  | YTD SOC SEC TIPS WAGES |
| 130 | MG045 | D9 |  |  | ANNUAL WAGES |
| 139 | MG050 | D6 |  |  | SOC SEC TAX WITHHELD |
| 145 | MG055 | D9 |  |  | FED INCOME TAX WITHHELD |
| 154 | MG060 | D7 |  |  | ALLOCATE TIPS |
| 161 | MG065 | D9 |  |  | FRINGE BENEFITS |
| 170 | MG070 | A1 |  |  | PENSION PLAN INDICATOR |
| 171 | MG075 | A1 |  |  | DEF COMP INDICATOR |
| 172 | MG080 | D9 |  |  | DEF COMP |
| 181 | MG085 | D7 |  |  | DCB |
| 188 | MG090 | A1 |  |  | STATUTORY EMPLOYEE |
| 189 | MG095 | D8 |  |  | MEDICARE WAGES/TIPS |
| 197 | MG100 | D6 |  |  | MEDICARE TAX WITHHELD |
| 203 | MG105 | D9 |  |  | 401K "D" AMOUNT |
| 212 | MG110 | D8 |  |  | STATE INCOME TAX |
| 220 | MG115 | D9 |  |  | STATE WAGES |
| 229 | MG120 | A2 |  |  | NAME OF STATE |
| 231 | MG125 | A1 |  |  | TAX TYPE CODE |

### PMCTL - RECORD, declared A232, computed 232

CONTROL RECORD FOR PM10.DDF

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A214 |  |  |  |
| 214 | MGORG | D5 |  |  | LOCK FLAG |
| 219 | MGREC | D5 |  |  | RECORD COUNT |
| 224 | MGMAX | D5 |  |  | MAXIMUM COUNT |
| 229 | *(filler)* | A3 |  |  |  |

## POHDR.FD

### POHDR - RECORD, declared A84, computed 84

PURCHASE ORDER HEADER FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PHNUM | D5 | D5 |  | PURCHASE ORDER NUMBER |
| 5 | PHVND | D4 | D4 |  | VENDOR NUMBER |
| 9 | PHVNM | A30 | A30 |  | VENDOR NAME (USE 25 CHAR) |
| 39 | PHBYR | A20 | A20 |  | BUYER |
| 59 | PHDAT | D8 | D8 |  | DATE |
| 67 | PHSDT | D8 | D8 |  | SHIP DATE |
| 75 | PHACD | D8 | D8 |  | AUTO CANCEL DATE |
| 83 | PHDFG | A1 | A1 |  | DELETE FLAG |

### (overlay 1) - RECORD, computed 5 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PHNO2 | A5 |  |  | ALPHA PURCHASE ORDER NUMBER |

### PHCTL - RECORD, computed 84 bytes

CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A66 |  |  |  |
| 66 | PHORG | D5 | D5 |  | ORGANIZED COUNT |
| 71 | PHREC | D5 | D5 |  | RECORD COUNT |
| 76 | PHMAX | D5 | D5 |  | MAXIMUM # OF RECORDS |
| 81 | PHDEL | D3 | D3 |  | DELETE COUNT |

## POLIN.FD

### POLIN - RECORD, declared A79, computed 79

PURCHASE ORDER LINE ITEM FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PLNUM | D5 | D5 |  | PURCHASE ORDER NUMBER |
| 5 | PLITM | D7 | D7 |  | ITEM NUMBER |
| 12 | PLDSC | A30 | A30 |  | DESCRIPTION |
| 42 | PLORD | D6 | D6 |  | QUANTITY ORDERED |
| 48 | PLCST | D8 | D8.2 |  | COST |
| 56 | PLRTL | D8 | D8.2 |  | RETAIL |
| 64 | PLDFG | A1 | A1 |  | DELETE FLAG |
| 65 | PLRCV | D6 | D6 |  | QUANTITY RECEIVED TO DATE |
| 71 | PLDAT | D8 | D8 |  | DATE OF LAST RECEIPT |

### PLCTL - RECORD, computed 79 bytes

CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A61 |  |  |  |
| 61 | PLORG | D5 | D5 |  | ORGANIZED COUNT |
| 66 | PLREC | D5 | D5 |  | RECORD COUNT |
| 71 | PLMAX | D5 | D5 |  | MAXIMUM # OF RECORDS |
| 76 | PLDEL | D3 | D3 |  | DELETE COUNT |

## PORCT.FD

### PORCT - RECORD, declared A87, computed 87

PURCHASE ORDER RECEIPTS WORK FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PRNUM | D5 | D5 |  | PURCHASE ORDER NUMBER |
| 5 | PRITM | D7 | D7 |  | ITEM NUMBER |
| 12 | PRORD | D6 | D6 |  | QUANTITY ORDERED |
| 18 | PROCS | D8 | D8.2 |  | ORDERED COST |
| 26 | PRRCV | D6 | D6 |  | QUANTITY RECEIVED |
| 32 | PRRCS | D8 | D8.2 |  | RECEIVED COST |
| 40 | PRRTL | D8 | D8.2 |  | RETAIL |
| 48 | PRCFG | A1 | A1 |  | COMPLETE FLAG |
| 49 | PRDSC | A30 | A30 |  | LINE ITEM DESCRIPTION |
| 79 | PRDAT | D8 | D8 |  | DATE RECEIVED |

### PRCTL - RECORD, computed 87 bytes

CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A69 |  |  |  |
| 69 | PRORG | D5 | D5 |  | ORGANIZED COUNT |
| 74 | PRREC | D5 | D5 |  | RECORD COUNT |
| 79 | PRMAX | D5 | D5 |  | MAXIMUM # OF RECORDS |
| 84 | PRDEL | D3 | D3 |  | DELETE COUNT |

## PPDTM.FD

### PPDTM - RECORD, declared A116, computed 116

TEMPORARY PRE-PAID FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PPVND | D4 | D4 |  | VENDOR NUMBER |
| 4 | PPVCH | D6 | D6 |  | VOUCHER NUMBER |
| 10 | PPINO | A35 | A35 |  | INVOICE NUMBER |
| 45 | PPIDT | D8 | D8 |  | INVOICE DATE |
| 53 | PPAMT | D10 | D10.2 |  | INVOICE AMOUNT |
| 63 | PPDSC | D8 | D8.2 |  | DISCOUNT AMOUNT |
| 71 | PPDDT | D8 | D8 |  | DUE DATE |
| 79 | PPSTF | D1 | D1 |  | STATUS FLAG |
| 80 | PPCHK | D6 | D6 |  | CHECK NUMBER |
| 86 | PPJOB | D4 | D4 |  | JOB NUMBER |
| 90 | PPPDD | D8 | D8 |  | PARTIAL PAY DUE DATE |
| 98 | PPPAM | D10 | D10.2 |  | PARTIAL PAY AMOUNT |
| 108 | PPPDS | D8 | D8.2 |  | PARTIAL PAY DISCOUNT |

### (overlay 1) - RECORD, computed 116 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A16 |  |  |  |
| 16 | PPINT | D1 |  |  | INTERFACE FLAG |
| 17 | *(filler)* | A94 |  |  |  |
| 111 | PPREC | D5 |  |  | NUMBER OF DATA RECORDS IN FILE |

## PRCMT.FD

### PRCMT - RECORD, declared A45, computed 45

PRICE MATRIX FILE (PRCMT.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PMCDE | D4 | A4 |  | PRICE MATRIX DISCOUNT CODE |
| 4 | PMPER | 20D2 | A40 |  | DISCOUNT PERCENT |
| 44 | PMDLF | A1 | A1 |  | DELETE FLAG |

### (overlay 1) - RECORD, computed 4 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PMCD2 | A4 |  |  | ALPHA DISCOUNT CODE |

### PMCTL - RECORD, computed 45 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A25 |  |  |  |
| 25 | PMDFG | D1 |  |  | DELETE FLAG |
| 26 | PMSFG | D1 |  |  | SORT FLAG |
| 27 | PMORG | D5 |  |  | ORGANIZE COUNT |
| 32 | PMREC | D5 |  |  | RECORD COUNT |
| 37 | PMMAX | D5 |  |  | MAXIMUM COUNT |
| 42 | PMDEL | D3 |  |  | DELETE COUNT |

## PRELG.FD

### PRELG - RECORD, declared A59, computed 59

PREL.DDF - TEMP ELIGIBILITY FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PE005 | D4 | D4.0 |  | EMPLOYEE NUMBER |
| 4 | PE010 | A15 | A15 |  | SHORT NAME |
| 19 | PE015 | D9 | D9.0 |  | SOCIAL SECURITY NUMBER |
| 28 | PE020 | D8 | D8.0 |  | DATE OF BIRTH |
| 36 | PE025 | D8 | D8.0 |  | DATE OF EMPLOYMENT |
| 44 | PE030 | D8 | D8.0 |  | DATE OF TERMINATION |
| 52 | PE035 | D6 | D6.2 |  | TOTAL HOURS YTD |
| 58 | PE040 | A1 | A1 |  | SALARY CODE |

### PECTL - RECORD, declared A59, computed 59

CONTROL RECORD FOR PREL.DDF

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A41 |  |  |  |
| 41 | PCORG | D5 |  |  | LOCK FLAG |
| 46 | PCREC | D5 |  |  | RECORD COUNT |
| 51 | PCMAX | D5 |  |  | MAXIMUM COUNT |
| 56 | *(filler)* | A3 |  |  |  |

## PRGL.FD

### PRGL - RECORD, declared A130, computed 130

PAYROLL TO G/L FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PRAMT | D10 | D10.2 |  | CHECK AMOUNT |
| 10 | PRSWG | D10 | D10.2 |  | SALARIED WAGES |
| 20 | PRHWG | D10 | D10.2 |  | HOURLY WAGES |
| 30 | PRFIC | D10 | D10.2 |  | FICA |
| 40 | PRFWT | D10 | D10.2 |  | FWT |
| 50 | PRSWT | D10 | D10.2 |  | SWT |
| 60 | PRSDI | D10 | D10.2 |  | SDI |
| 70 | PRCWT | D10 | D10.2 |  | CWT |
| 80 | PRINS | D10 | D10.2 |  | INSURANCE |
| 90 | PRUNN | D10 | D10.2 |  | UNION DUES |
| 100 | PRSVB | D10 | D10.2 |  | SAVINGS BONDS |
| 110 | PRMSC | D10 | D10.2 |  | MISCELLANEOUS |
| 120 | PRMLS | D10 | D10.2 |  | MEALS |

## PRTIF.FD

### PRTIF - RECORD, declared A101, computed 101

PARTIAL PAYMENTS (PRTIF.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PTVND | D4 | D4 |  | VENDOR NUMBER |
| 4 | PTVCH | D6 | D6 |  | VOUCHER NUMBER |
| 10 | PTINO | A35 | A35 |  | INVOICE NUMBER |
| 45 | PTIDT | D8 | D8 |  | INVOICE DATE |
| 53 | PTAMT | D10 | D10 |  | INVOICE AMOUNT |
| 63 | PTDSC | D8 | D8 |  | DISCOUNT AMOUNT |
| 71 | PTDDT | D8 | D8 |  | DUE DATE |
| 79 | PTPAY | D10 | D10 |  | PARTIAL PAYMENT AMOUNT |
| 89 | PTPDS | D8 | D8 |  | PARTIAL PAYMENT DISC AMOUNT |
| 97 | PTJOB | D4 | D4 |  | JOB NUMBER |

### PTCTL - RECORD, computed 101 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A83 |  |  |  |
| 83 | PTORG | D5 |  |  | ORGANIZE COUNT |
| 88 | PTREC | D5 |  |  | RECORD COUNT |
| 93 | PTMAX | D5 |  |  | MAXIMUM COUNT |
| 98 | PTDEL | D3 |  |  | DELETE COUNT |

## PTCON.FD

### PTCON - RECORD, declared A80, computed 80

PTCO.DDF - 401K TRANSFER FILE (PTCON.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | TC005 | A8 |  |  | COMPANY NAME |
| 8 | TC010 | A4 |  |  | EMPLOYEE NUMBER |
| 12 | TC015 | A15 |  |  | SHORT NAME |
| 27 | TC020 | A11 |  |  | SOC SEC # |
| 38 | TC025 | A1 |  |  | HOURLY/SALARY CODE |
| 39 | TC030 | A8 |  |  | MONTHLY GROSS WAGES |
| 47 | TC035 | A7 |  |  | MONTHLY HOURS WORKED |
| 54 | TC040 | A8 |  |  | MONTHLY CAFETERIA |
| 62 | TC045 | A8 |  |  | MONTHLY 401K |
| 70 | TC050 | A10 |  |  | 401K EMPLOYEE PERCENT |

### TCCTL - RECORD, declared A80, computed 80

CONTROL RECORD FOR PTCO.DDF

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A62 |  |  |  |
| 62 | TCORG | D5 |  |  | LOCK FLAG |
| 67 | TCREC | D5 |  |  | RECORD COUNT |
| 72 | TCMAX | D5 |  |  | MAXIMUM COUNT |
| 77 | *(filler)* | A3 |  |  |  |

## PTR10.FD

### PTR10 - RECORD, declared A80, computed 80

PTR1.DDF - 401K TRANSFER FILE (PTR10.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | TR005 | A8 |  |  | COMPANY NAME |
| 8 | TR010 | A4 |  |  | EMPLOYEE NUMBER |
| 12 | TR015 | A15 |  |  | SHORT NAME |
| 27 | TR020 | A11 |  |  | SOC SEC # |
| 38 | TR025 | A1 |  |  | HOURLY/SALARY CODE |
| 39 | TR030 | A8 |  |  | MONTHLY GROSS WAGES |
| 47 | TR035 | A7 |  |  | MONTHLY HOURS WORKED |
| 54 | TR040 | A8 |  |  | MONTHLY CAFETERIA |
| 62 | TR045 | A8 |  |  | MONTHLY 401K |
| 70 | TR050 | A10 |  |  | 401K EMPLOYEE PERCENT |

### TRCTL - RECORD, declared A80, computed 80

CONTROL RECORD FOR PTR1.DDF

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A62 |  |  |  |
| 62 | TRORG | D5 |  |  | LOCK FLAG |
| 67 | TRREC | D5 |  |  | RECORD COUNT |
| 72 | TRMAX | D5 |  |  | MAXIMUM COUNT |
| 77 | *(filler)* | A3 |  |  |  |

## PURCM.FD

### PURCM - RECORD, declared A120, computed 120

PURCHASES FILE (PURCM.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PCONO | D5 | D5 |  | PURCHASE ORDER NUMBER |
| 5 | PCITM | A10 | A10 |  | ITEM NUMBER |
| 15 | PCDSC | A30 | A30 |  | ITEM DESCRIPTION |
| 45 | PCOQH | D6 | D6 |  | OLD QUANTITY ON HAND |
| 51 | PCOCS | D7 | D7 |  | OLD COST |
| 58 | PCOPC | D7 | D7 |  | OLD PRICE |
| 65 | PCOQO | D6 | D6 |  | OLD QUANTITY ORDER |
| 71 | PCOQC | D6 | D6 |  | OLD QUANTITY COMMITTED |
| 77 | PCQPY | D6 | D6 |  | QUANTITY PURCHASED |
| 83 | PCQCM | D6 | D6 |  | QUANTITY COMMMITTED |
| 89 | PCNQO | D6 | D6 |  | NEW QUANTITY ORDER |
| 95 | PCNQC | D6 | D6 |  | NEW QUANTITY COMMITTED |
| 101 | PCSYD | D8 | D8 |  | SALES YTD |
| 109 | PCREL | D6 | D6 |  | RE-ORDER LEVEL |
| 115 | *(filler)* | A5 | A5 |  | SLUSH |

### PCCTL - RECORD, computed 120 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A102 |  |  |  |
| 102 | PCORG | D5 |  |  | ORGANIZE COUNT |
| 107 | PCREC | D5 |  |  | RECORD COUNT |
| 112 | PCMAX | D5 |  |  | MAXIMUM COUNT |
| 117 | PCDEL | D3 |  |  | DELETE COUNT |

## PURGE.FD

### PURGE - RECORD, declared A83, computed 83

PURGE ITEMS FROM A/P OPEN (PURGE.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PGVND | D4 | D4 |  | VENDOR NUMBER |
| 4 | PGVCH | D6 | D6 |  | VOUCHER NUMBER |
| 10 | PGINO | A35 | A35 |  | INVOICE NUMBER |
| 45 | PGIDT | D8 | D8 |  | INVOICE DATE |
| 53 | PGAMT | D10 | D10 |  | INVOICE AMOUNT |
| 63 | PGDSC | D8 | D8 |  | DISCOUNT AMOUNT |
| 71 | PGDDT | D8 | D8 |  | DUE DATE |
| 79 | PGJOB | D4 | D4 |  | JOB NUMBER |

### PGCTL - RECORD, computed 83 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A70 |  |  |  |
| 70 | PGREC | D5 |  |  | RECORD COUNT |
| 75 | *(filler)* | A8 |  |  |  |

## PURIX.FD

### PURIX - RECORD, declared A24, computed 24

PURGE INDEX (PURIX.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | PICNO | A5 | A5 |  | CUSTOMER NUMBER |
| 5 | PIAPL | D6 | D6 |  | APPLY TO NUMBER |
| 11 | PIAMT | D8 | D8 |  | AMOUNT |
| 19 | PIRNO | D5 | D5 |  | RECORD NUMBER |

### PICTL - RECORD, computed 24 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A6 |  |  |  |
| 6 | PIORG | D5 |  |  | ORGANIZE COUNT |
| 11 | PIREC | D5 |  |  | RECORD COUNT |
| 16 | PIMAX | D5 |  |  | MAXIMUM COUNT |
| 21 | PIDEL | D3 |  |  | DELETE COUNT |

## PWHDR.FD

### PWHDR - RECORD, declared A84, computed 84

PURCHASE ORDER HEADER WORK FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | WHNUM | D5 | D5 |  | PURCHASE ORDER NUMBER |
| 5 | WHVND | D4 | D4 |  | VENDOR NUMBER |
| 9 | WHVNM | A30 | A30 |  | VENDOR NAME (USE 25 CHAR) |
| 39 | WHBYR | A20 | A20 |  | BUYER |
| 59 | WHDAT | D8 | D8 |  | DATE |
| 67 | WHSDT | D8 | D8 |  | SHIP DATE |
| 75 | WHACD | D8 | D8 |  | AUTO CANCEL DATE |
| 83 | WHDFG | A1 | A1 |  | DELETE FLAG |

### WHCTL - RECORD, computed 84 bytes

CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A66 |  |  |  |
| 66 | WHORG | D5 | D5 |  | ORGANIZED COUNT |
| 71 | WHREC | D5 | D5 |  | RECORD COUNT |
| 76 | WHMAX | D5 | D5 |  | MAXIMUM # OF RECORDS |
| 81 | WHDEL | D3 | D3 |  | DELETE COUNT |

## PWLIN.FD

### PWLIN - RECORD, declared A79, computed 79

PURCHASE ORDER LINE ITEM WORK FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | WLNUM | D5 | D5 |  | PURCHASE ORDER NUMBER |
| 5 | WLITM | D7 | D7 |  | ITEM NUMBER |
| 12 | WLDSC | A30 | A30 |  | DESCRIPTION |
| 42 | WLORD | D6 | D6 |  | QUANTITY ORDERED |
| 48 | WLCST | D8 | D8.2 |  | COST |
| 56 | WLRTL | D8 | D8.2 |  | RETAIL |
| 64 | WLDFG | A1 | A1 |  | DELETE FLAG |
| 65 | WLRCV | D6 | D6 |  | QUANTITY RECEIVED TO DATE |
| 71 | WLDAT | D8 | D8 |  | DATE OF LAST RECEIPT |

### WLCTL - RECORD, computed 79 bytes

CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A60 |  |  |  |
| 60 | WLSFG | D1 | D1 |  | SORT FLAG |
| 61 | WLORG | D5 | D5 |  | ORGANIZED COUNT |
| 66 | WLREC | D5 | D5 |  | RECORD COUNT |
| 71 | WLMAX | D5 | D5 |  | MAXIMUM # OF RECORDS |
| 76 | WLDEL | D3 | D3 |  | DELETE COUNT |

## SAIDX.FD

### SAIDX - RECORD, declared A16, computed 16

SALES ANALYSIS INDEX (SAIDX.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | SACNO | A5 | A5 |  | CUSTOMER NUMBER |
| 5 | SASLS | D2 | D2 |  | SALESMAN NUMBER |
| 7 | SACTP | A2 | A2 |  | CUSTOMER TYPE |
| 9 | SASCD | A2 | A2 |  | STATE CODE |
| 11 | SARNO | D5 | D5 |  | RECORD NUMBER |

## SALCT.FD

### SALCT - RECORD, declared A87, computed 87

SALESMAN CATEGORY FILE (SALCT.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | SMSLS | D2 | D2 |  | SALESMAN |
| 2 | SMSCT | D3 | D3 |  | SALES CATEGORY |
| 5 | SMSMD | D10 | D10 |  | SALES MTD |
| 15 | SMCMD | D10 | D10 |  | COST MTD |
| 25 | SMQMD | D10 | D10 |  | QUANTITY MTD |
| 35 | SMSYD | D10 | D10 |  | SALES YTD |
| 45 | SMCYD | D10 | D10 |  | COST YTD |
| 55 | SMQYD | D10 | D10 |  | QUANTITY YTD |
| 65 | SMDFG | A1 | A1 |  | SLUSH |
| 66 | SMCPT | D4 | D4 |  | COMM PERCENT |
| 70 | SMCPS | D8 | D8 |  | COMM PERIOD SALES |
| 78 | SMCPC | D8 | D8 |  | COMM PERIOD COST |
| 86 | SMCCL | A1 | A1 |  | COMM CALCULATION |

### SMCTL - RECORD, computed 87 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A69 |  |  |  |
| 69 | SMORG | D5 |  |  | ORGANIZE COUNT |
| 74 | SMREC | D5 |  |  | RECORD COUNT |
| 79 | SMMAX | D5 |  |  | MAXIMUM COUNT |
| 84 | SMDEL | D3 |  |  | DELETE COUNT |

## SALES.FD

### SALES - RECORD, declared A1878, computed 1878

SALES FILE (SALES.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | SLDNO | D6 | D6 |  | DOCUMENT NUMBER |
| 6 | SLDTP | D1 | D1 |  | DOCUMENT TYPE |
| 7 | SLDDT | D8 | D8 |  | DOCUMENT DATE |
| 15 | SLCNO | A5 | A5 |  | CUSTOMER NUMBER |
| 20 | SLCNM | A25 | A25 |  | CUSTOMER NAME |
| 45 | SLSLS | D2 | D2 |  | SALESMAN NUMBER |
| 47 | SLAMT | D8 | D8 |  | AMOUNT |
| 55 | SLMSC | D6 | D6 |  | MISC AMOUNT |
| 61 | SLTAX | D7 | D7 |  | TAX AMOUNT |
| 68 | SLFRT | D6 | D6 |  | FREIGHT |
| 74 | SLCST | D8 | D8 |  | COST |
| 82 | SLAPL | D6 | D6 |  | APPLY TO NUMBER |
| 88 | SLSCD | A2 | A2 |  | STATE TAX CODE |
| 90 | SLCCD | D3 | D3 |  | CITY TAX CODE |
| 93 | SLTFG | A1 | A1 |  | TAX FLAG |
| 94 | SLTAM | D8 | D8 |  | TAXABLE AMOUNT |
| 102 | SLJOB | D6 | D6 |  | NUMBER OF JOBS |
| 108 | SLCAT | 30A7 | A210 |  | SALES CATEGORIES |
| 318 | SLCQT | 30D6 | A180 |  | CATEGORY QUANTITY |
| 498 | SLDSC | 30A30 | A900 |  | DISCRIPTION |
| 1398 | SLCPR | 30D7 | A210 |  | CATEGORY PRICE |
| 1608 | SLCCT | 30D7 | A210 |  | CATEGORY COST |
| 1818 | SLDIS | 30D2 | A60 |  | DISCOUNT PERCENT |

### (overlay 1) - RECORD, computed 6 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | SLDN2 | A6 |  |  | ALPHA DOCUMENT NUMBER |

### SLCTL - RECORD, computed 1878 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1853 |  |  |  |
| 1853 | SLPST | A1 |  |  | POSTING FLAG I = INVOICE T = TICKET S = SALES |
| 1854 | SLDDC | D6 |  |  | DEFAULT DOCUMENT NUMBER |
| 1860 | SLORG | D5 |  |  | ORGANIZE COUNT |
| 1865 | SLREC | D5 |  |  | RECORD COUNT |
| 1870 | SLMAX | D5 |  |  | MAXIMUM COUNT |
| 1875 | SLDEL | D3 |  |  | DELETE COUNT |

## SALES.FDC

### SALES - COMMON, declared A1878, computed 1878

SALES FILE (SALES.FDC)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | SLDNO | D6 | D6 |  | DOCUMENT NUMBER |
| 6 | SLDTP | D1 | D1 |  | DOCUMENT TYPE |
| 7 | SLDDT | D8 | D8 |  | DOCUMENT DATE |
| 15 | SLCNO | A5 | A5 |  | CUSTOMER NUMBER |
| 20 | SLCNM | A25 | A25 |  | CUSTOMER NAME |
| 45 | SLSLS | D2 | D2 |  | SALESMAN NUMBER |
| 47 | SLAMT | D8 | D8 |  | AMOUNT |
| 55 | SLMSC | D6 | D6 |  | MISC AMOUNT |
| 61 | SLTAX | D7 | D7 |  | TAX AMOUNT |
| 68 | SLFRT | D6 | D6 |  | FREIGHT |
| 74 | SLCST | D8 | D8 |  | COST |
| 82 | SLAPL | D6 | D6 |  | APPLY TO NUMBER |
| 88 | SLSCD | A2 | A2 |  | STATE TAX CODE |
| 90 | SLCCD | D3 | D3 |  | CITY TAX CODE |
| 93 | SLTFG | A1 | A1 |  | TAX FLAG |
| 94 | SLTAM | D8 | D8 |  | TAXABLE AMOUNT |
| 102 | SLJOB | D6 | D6 |  | NUMBER OF JOBS |
| 108 | SLCAT | 30A7 | A210 |  | SALES CATEGORIES |
| 318 | SLCQT | 30D6 | A180 |  | CATEGORY QUANTITY |
| 498 | SLDSC | 30A30 | A900 |  | DISCRIPTION |
| 1398 | SLCPR | 30D7 | A210 |  | CATEGORY PRICE |
| 1608 | SLCCT | 30D7 | A210 |  | CATEGORY COST |
| 1818 | SLDIS | 30D2 | A60 |  | DISCOUNT PERCENT |

### (overlay 1) - COMMON, computed 6 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | SLDN2 | A6 |  |  | ALPHA DOCUMENT NUMBER |

### SLCTL - COMMON, computed 1878 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1853 |  |  |  |
| 1853 | SLPST | A1 |  |  | POSTING FLAG I = INVOICE T = TICKET S = SALES |
| 1854 | SLDDC | D6 |  |  | DEFAULT DOCUMENT NUMBER |
| 1860 | SLORG | D5 |  |  | ORGANIZE COUNT |
| 1865 | SLREC | D5 |  |  | RECORD COUNT |
| 1870 | SLMAX | D5 |  |  | MAXIMUM COUNT |
| 1875 | SLDEL | D3 |  |  | DELETE COUNT |

## SCREEN.FDC

### SMOV - COMMON, computed 8 bytes

MOVE CURSOR POSITION (VT100)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1 |  | . |  |
| 1 | *(filler)* | A1 |  | [ |  |
| 2 | SROW | A2 |  | 00 |  |
| 4 | *(filler)* | A1 |  | ; |  |
| 5 | SCOL | A2 |  | 00 |  |
| 7 | *(filler)* | A1 |  | H |  |

### SNOR - COMMON, computed 4 bytes

SCREEN NORMAL MODE (VT100)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1 |  | . |  |
| 1 | *(filler)* | A1 |  | [ |  |
| 2 | *(filler)* | A1 |  | 0 |  |
| 3 | *(filler)* | A1 |  | m |  |

### SREV - COMMON, computed 4 bytes

SCREEN REVERSE MODE (VT100)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1 |  | . |  |
| 1 | *(filler)* | A1 |  | [ |  |
| 2 | *(filler)* | A1 |  | 7 |  |
| 3 | *(filler)* | A1 |  | m |  |

### SBOL - COMMON, computed 4 bytes

SCREEN BOLD MODE (VT100)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1 |  | . |  |
| 1 | *(filler)* | A1 |  | [ |  |
| 2 | *(filler)* | A1 |  | 1 |  |
| 3 | *(filler)* | A1 |  | m |  |

### SHID - COMMON, computed 6 bytes

HIDE CURSOR POSITION (VT100)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1 |  | . |  |
| 1 | *(filler)* | A1 |  | [ |  |
| 2 | *(filler)* | A1 |  | ? |  |
| 3 | *(filler)* | A2 |  | 25 |  |
| 5 | *(filler)* | A1 |  | l |  |

### SSHO - COMMON, computed 6 bytes

SHOW CURSOR POSITION (VT100)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1 |  | . |  |
| 1 | *(filler)* | A1 |  | [ |  |
| 2 | *(filler)* | A1 |  | ? |  |
| 3 | *(filler)* | A2 |  | 25 |  |
| 5 | *(filler)* | A1 |  | h |  |

### SGM0 - COMMON, computed 3 bytes

SCREEN GRAPHICS RESET (VT100)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1 |  | . |  |
| 1 | *(filler)* | A1 |  | ( |  |
| 2 | *(filler)* | A1 |  | B |  |

### SGM1 - COMMON, computed 3 bytes

SCREEN GRAPHICS SET (VT100)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1 |  | . |  |
| 1 | *(filler)* | A1 |  | ( |  |
| 2 | *(filler)* | A1 |  | 0 |  |

### SOPE - COMMON, computed 3 bytes

OPEN NEW LINE (VT100)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1 |  | . |  |
| 1 | *(filler)* | A1 |  | [ |  |
| 2 | *(filler)* | A1 |  | L |  |

### SHOM - COMMON, computed 3 bytes

GO HOME (VT100)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1 |  | . |  |
| 1 | *(filler)* | A1 |  | [ |  |
| 2 | *(filler)* | A1 |  | H |  |

### SCLR - COMMON, computed 3 bytes

CLEAR SCREEN (VT100)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1 |  | . |  |
| 1 | *(filler)* | A1 |  | [ |  |
| 2 | *(filler)* | A1 |  | J |  |

### SCLN - COMMON, computed 3 bytes

CLEAN LINE (VT100)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1 |  | . |  |
| 1 | *(filler)* | A1 |  | [ |  |
| 2 | *(filler)* | A1 |  | K |  |

### SWIN - COMMON, computed 8 bytes

SET SCROLLING REGION (VT100)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1 |  | . |  |
| 1 | *(filler)* | A1 |  | [ |  |
| 2 | STOP | A2 |  | 00 |  |
| 4 | *(filler)* | A1 |  | ; |  |
| 5 | SBOT | A2 |  | 00 |  |
| 7 | *(filler)* | A1 |  | r |  |

### SMES - COMMON, computed 8 bytes

MOVE CURSOR TO MESSAGE POSITION (VT100)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1 |  | . |  |
| 1 | *(filler)* | A1 |  | [ |  |
| 2 | *(filler)* | A2 |  | 23 |  |
| 4 | *(filler)* | A1 |  | ; |  |
| 5 | *(filler)* | A2 |  | 01 |  |
| 7 | *(filler)* | A1 |  | H |  |

### SMOV - COMMON, computed 8 bytes

MOVE CURSOR POSITION (FANSI)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1 |  | . |  |
| 1 | *(filler)* | A1 |  | [ |  |
| 2 | SROW | A2 |  | 00 |  |
| 4 | *(filler)* | A1 |  | ; |  |
| 5 | SCOL | A2 |  | 00 |  |
| 7 | *(filler)* | A1 |  | H |  |

### SNOR - COMMON, computed 4 bytes

SCREEN NORMAL MODE (FANSI)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1 |  | . |  |
| 1 | *(filler)* | A1 |  | [ |  |
| 2 | *(filler)* | A1 |  | 0 |  |
| 3 | *(filler)* | A1 |  | m |  |

### SREV - COMMON, computed 8 bytes

SCREEN REVERSE MODE (FANSI)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1 |  | . |  |
| 1 | *(filler)* | A1 |  | [ |  |
| 2 | *(filler)* | A2 |  | 46 |  |
| 4 | *(filler)* | A1 |  | ; |  |
| 5 | *(filler)* | A2 |  | 30 |  |
| 7 | *(filler)* | A1 |  | m |  |

### SBOL - COMMON, computed 8 bytes

SCREEN BOLD MODE (FANSI)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1 |  | . |  |
| 1 | *(filler)* | A1 |  | [ |  |
| 2 | *(filler)* | A2 |  | 47 |  |
| 4 | *(filler)* | A1 |  | ; |  |
| 5 | *(filler)* | A2 |  | 31 |  |
| 7 | *(filler)* | A1 |  | m |  |

### SHID - COMMON, computed 6 bytes

HIDE CURSOR POSITION (FANSI)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1 |  | . |  |
| 1 | *(filler)* | A1 |  | [ |  |
| 2 | *(filler)* | A1 |  | > |  |
| 3 | *(filler)* | A2 |  | 22 |  |
| 5 | *(filler)* | A1 |  | h |  |

### SSHO - COMMON, computed 6 bytes

SHOW CURSOR POSITION (FANSI)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1 |  | . |  |
| 1 | *(filler)* | A1 |  | [ |  |
| 2 | *(filler)* | A1 |  | > |  |
| 3 | *(filler)* | A2 |  | 22 |  |
| 5 | *(filler)* | A1 |  | l |  |

### SGM0 - COMMON, computed 3 bytes

SCREEN GRAPHICS RESET (FANSI)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1 |  | . |  |
| 1 | *(filler)* | A1 |  | ( |  |
| 2 | *(filler)* | A1 |  | B |  |

### SGM1 - COMMON, computed 3 bytes

SCREEN GRAPHICS SET (FANSI)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1 |  | . |  |
| 1 | *(filler)* | A1 |  | ( |  |
| 2 | *(filler)* | A1 |  | 0 |  |

### SOPE - COMMON, computed 3 bytes

OPEN NEW LINE (FANSI)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1 |  | . |  |
| 1 | *(filler)* | A1 |  | [ |  |
| 2 | *(filler)* | A1 |  | T |  |

### SHOM - COMMON, computed 3 bytes

GO HOME (FANSI)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1 |  | . |  |
| 1 | *(filler)* | A1 |  | [ |  |
| 2 | *(filler)* | A1 |  | H |  |

### SCLR - COMMON, computed 3 bytes

CLEAR SCREEN (FANSI)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1 |  | . |  |
| 1 | *(filler)* | A1 |  | [ |  |
| 2 | *(filler)* | A1 |  | J |  |

### SCLN - COMMON, computed 3 bytes

CLEAN LINE (FANSI)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1 |  | . |  |
| 1 | *(filler)* | A1 |  | [ |  |
| 2 | *(filler)* | A1 |  | K |  |

### SWIN - COMMON, computed 8 bytes

SET SCROLLING REGION (FANSI)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1 |  | . |  |
| 1 | *(filler)* | A1 |  | [ |  |
| 2 | STOP | A2 |  | 00 |  |
| 4 | *(filler)* | A1 |  | ; |  |
| 5 | SBOT | A2 |  | 00 |  |
| 7 | *(filler)* | A1 |  | r |  |

### SMES - COMMON, computed 8 bytes

MOVE CURSOR TO MESSAGE POSITION (FANSI)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A1 |  | . |  |
| 1 | *(filler)* | A1 |  | [ |  |
| 2 | *(filler)* | A2 |  | 23 |  |
| 4 | *(filler)* | A1 |  | ; |  |
| 5 | *(filler)* | A2 |  | 01 |  |
| 7 | *(filler)* | A1 |  | H |  |

## SECUR.FD

### SECUR - RECORD, declared A188, computed 188

PROGRAM SECURITY INFORMATION

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | SR05 | A9 |  |  | PROGRAM NAME |
| 9 | SR10 | A50 |  |  | PROGRAM DESCRIPTION |
| 59 | SR15 | A1 |  |  | PROGRAM FLAG: |
| 60 | SR20 | 128A1 |  |  | SECURITY FLAG VALUES: |

## SRCIX.FD

### SRCIX - RECORD, declared A16, computed 16

SOURCE CROSS REFERENCE INDEX

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | SCSRC | A3 | A3 |  | TRANSACTION SOURCE |
| 3 | SCDAT | D8 | D8 |  | TRANSACTION DATE |
| 11 | SCREC | D5 | D5 |  | RECORD # IN YTD TRX FILE |

## STATE.FD

### STATE - RECORD, declared A73, computed 73

MTD STATE TAX FILE (STATE.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | STCOD | A2 | A2 |  | STATE CODE |
| 2 | STPER | D4 | D4 |  | STATE PERCENT |
| 6 | STNAM | A20 | A20 |  | STATE NAME |
| 26 | STAAM | D10 | D10 |  | A AMOUNT |
| 36 | STCAM | D10 | D10 |  | C AMOUNT |
| 46 | STKAM | D10 | D10 |  | K AMOUNT |
| 56 | STTAM | D10 | D10 |  | T AMOUNT |
| 66 | STGLN | D7 | D7 |  | G/L NUMBER |

## SYSTEM.FD

### (overlay 0) - RECORD, computed 5 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | UNIX | A1 |  |  | OPERATING SYSTEM |
| 1 | VT100 | A1 |  |  | TERMINAL TYPE |
| 2 | BNKREC | A1 |  |  | BANK REC USED IN A/P AND PAYROLL |
| 3 | RPLCST | A1 |  |  | REPLACE UNIT COST WITH RECEIVINGS COST |
| 4 | SCCMP | A1 |  |  | SECURITY BY COMPANY NUMBER |

## SYSTEM.FDC

### (overlay 0) - COMMON, computed 5 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | UNIX | A1 |  |  | OPERATING SYSTEM |
| 1 | VT100 | A1 |  |  | TERMINAL TYPE/SYSTEM |
| 2 | BNKREC | A1 |  |  | BANK REC USED IN A/P AND PAYROLL |
| 3 | RPLCST | A1 |  |  | REPLACE UNIT COST WITH RECEIVINGS COST |
| 4 | SCCMP | A1 |  |  | SECURITY BY COMPANY NUMBER |

## TCASH.FD

### TCASH - RECORD, declared A80, computed 80

CASH RECEIPTS FILE (TCASH.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | CHCNO | A5 | A5 |  | CUSTOMER NUMBER |
| 5 | CHCNM | A25 | A25 |  | CUSTOMER NAME |
| 30 | CHRDT | D8 | D8 |  | RECEIPT DATE |
| 38 | CHCKN | D6 | D6 |  | CHECK NUMBER |
| 44 | CHAMT | D8 | D8 |  | AMOUNT RECEIVED |
| 52 | CHDIS | D7 | D7 |  | DISCOUNT AMOUNT |
| 59 | CHAPL | D6 | D6 |  | APPLY TO NUMBER |
| 65 | CHMSC | D8 | D8 |  | MISC AMOUNT |
| 73 | CHGLA | D7 | D7 |  | GENERAL LEDGER NUMBER |

### CHCTL - RECORD, computed 80 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A62 |  |  |  |
| 62 | CHORG | D5 |  |  | ORGANIZE COUNT |
| 67 | CHREC | D5 |  |  | RECORD COUNT |
| 72 | CHMAX | D5 |  |  | MAXIMUM COUNT |
| 77 | CHDEL | D3 |  |  | DELETE COUNT |

## TGLIX.FD

### TGLIX - RECORD, declared A16, computed 16

SUPPORTING SCHEDULE INDEX

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | TISSC | A7 | A7 |  | SUPPORTING SCHEDULE CODE |
| 7 | TIMAS | D4 | D4 |  | RECORD # IN G/L ACCOUNT MASTER |
| 11 | TIREC | D5 | D5 |  | REC # OF 1ST TRX IN YTDGL FILE |

### (overlay 1) - RECORD, computed 16 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | TISCH | D1 |  |  | TYPE OF SCHEDULE |
| 1 | *(filler)* | A15 |  |  |  |

## TMPA2.FD

### TMPA2 - RECORD, declared A74, computed 74

TEMPORARY A/P OPEN FILE (TMPAP.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | TSVND | D4 | D4 |  | VENDOR NUMBER |
| 4 | TSAMT | D10 | D10 |  | AMOUNT |
| 14 | TSDAT | D8 | D8 |  | CHECK DATE |
| 22 | TSSTF | D1 | D1 |  | STATUS FLAG |
| 23 | TSCHK | D6 | D6 |  | CHECK NUMBER |
| 29 | TSVCH | D6 | D6 |  | VOUCHER NUMBER |
| 35 | TSINO | A35 | A35 |  | INVOICE NUMBER |
| 70 | TSJOB | D4 | D4 |  | JOB NUMBER |

### TSCTL - RECORD, computed 74 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A56 |  |  |  |
| 56 | TSORG | D5 |  |  | ORGANIZE COUNT |
| 61 | TSREC | D5 |  |  | RECORD COUNT |
| 66 | TSMAX | D5 |  |  | MAXIMUM COUNT |
| 71 | TSDEL | D3 |  |  | DELETE COUNT |

## TMPAP.FD

### TMPAP - RECORD, declared A74, computed 74

TEMPORARY A/P OPEN FILE (TMPAP.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | TPVND | D4 | D4 |  | VENDOR NUMBER |
| 4 | TPAMT | D10 | D10 |  | AMOUNT |
| 14 | TPDAT | D8 | D8 |  | CHECK DATE |
| 22 | TPSTF | D1 | D1 |  | STATUS FLAG |
| 23 | TPCHK | D6 | D6 |  | CHECK NUMBER |
| 29 | TPVCH | D6 | D6 |  | VOUCHER NUMBER |
| 35 | TPINO | A35 | A35 |  | INVOICE NUMBER |
| 70 | TPJOB | D4 | D4 |  | JOB NUMBER |

### TPCTL - RECORD, computed 74 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A56 |  |  |  |
| 56 | TPORG | D5 |  |  | ORGANIZE COUNT |
| 61 | TPREC | D5 |  |  | RECORD COUNT |
| 66 | TPMAX | D5 |  |  | MAXIMUM COUNT |
| 71 | TPDEL | D3 |  |  | DELETE COUNT |

## TMPFL.FD

### TMPFL - RECORD, declared A196, computed 196

TEMPORARY G/L FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | TFCSL | D10 | D10.2 |  | CURRENT PERIOD SALES |
| 10 | TFYSL | D10 | D10.2 |  | YTD SALES |
| 20 | TFCCS | D10 | D10.2 |  | CUR PD BUDGETED/COMPARED SALES |
| 30 | TFYCS | D10 | D10.2 |  | YTD BUDGETED/COMPARED SALES |
| 40 | TFYPL | D10 | D10.2 |  | YTD P & L AMOUNT OR PRV PRD AMT |
| 50 | TFCPL | D10 | D10.2 |  | LAST YEAR'S (COMPARED) P & L AMOUNT |
| 60 | TFNAM | A35 | A35 |  | COMPANY NAME |
| 95 | TFSNO | D2 | D2 |  | CURRENT SCHEDULE TO PRINT |
| 97 | TFSCH | 99D1 | A99 |  | SUPPORTING SCHEDULES REQUESTED |

## TMPGL.FD

### TMPGL - RECORD, declared A49, computed 49

TEMPORARY G/L DISTRIBUTION FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | TGACT | D7 | D7 |  | G/L ACCOUNT NUMBER |
| 7 | TGVCH | D6 | D6 |  | VOUCHER NUMBER |
| 13 | TGVND | D4 | D4 |  | VENDOR NUMBER |
| 17 | TGIDT | D8 | D8 |  | INVOICE DATE |
| 25 | TGDDT | D8 | D8 |  | DUE DATE |
| 33 | TGCHK | D6 | D6 |  | CHECK NUMBER |
| 39 | TGAMT | D10 | D10.2 |  | DISTRIBUTION AMOUNT |

## TMPIX.FD

### TMPIX - RECORD, declared A30, computed 30

TEMPORARY INDEX OF CUSMAS FOR ALPHA LIST (TMPIX.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | TICNM | A25 | A25 |  | CUSTOMER NAME |
| 25 | TICNO | A5 | A5 |  | CUSTOMER NUMBER |

## TVNIX.FD

### TVNIX - RECORD, declared A29, computed 29

TEMPORARY ALPHA VENDOR INDEX (TVNIX.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | TVVND | A25 | A25 |  | VENDOR NAME |
| 25 | TVRNO | D4 | D4 |  | RECORD NUMBER IN VENDOR MASTER |

### TVCTL - RECORD, computed 29 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A11 |  |  |  |
| 11 | TVORG | D5 |  |  | ORGANIZE COUNT |
| 16 | TVREC | D5 |  |  | RECORD COUNT |
| 21 | TVMAX | D5 |  |  | MAXIMUM COUNT |
| 26 | TVDEL | D3 |  |  | DELETE COUNT |

## UNTMF.FD

### UNTMF - RECORD, declared A104, computed 104

UNIT COST MASTER FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | UNTNO | D7 |  |  | UNIT NUMBER |
| 7 | UEDOL | D10 |  |  | ORGINAL ESTIMATE DOLLARS |
| 17 | UERVD | D10 |  |  | REVISED ESTIMATE DOLLARS |
| 27 | UDTDR | D8 |  |  | DATE DOLLARS REVISED |
| 35 | UCURD | D10 |  |  | CURRENT PERIOD DOLLARS |
| 45 | UPTDD | D10 |  |  | PROJECT TO DATE DOLLARS |
| 55 | UEQTY | D10 |  |  | ORGINAL ESTIMATE QUANTITY |
| 65 | UERVQ | D10 |  |  | REVISED ESTIMATE QUANTITY |
| 75 | UDTQR | D8 |  |  | DATE QUANTITY REVISED |
| 83 | UCURQ | D10 |  |  | ACTUAL QUANTITY CURRENT PERIOD |
| 93 | UPTDQ | D10 |  |  | ACTUAL QUANTITY PROJECT TO DATE |
| 103 | UCOMP | A1 |  |  | PROJECT COMPLETE Y OR N |

### UMFCT - RECORD, computed 104 bytes

UNIT COST MASTER FILE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A84 |  |  |  |
| 84 | UMFSF | D1 |  |  | SORT FLAG |
| 85 | UMFDF | D1 |  |  | DELETE FLAG |
| 86 | UMFOC | D5 |  |  | ORGANIZED COUNT |
| 91 | UMFRC | D5 |  |  | RECORD COUNT |
| 96 | UMFMX | D5 |  |  | MAXIMUM RECORD COUNT |
| 101 | UMFDC | D3 |  |  | DELETE COUNT |

## UNTMF.FDC

### UNTMF - COMMON, declared A104, computed 104

UNIT COST MASTER FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | UNTNO | D7 |  |  | UNIT NUMBER |
| 7 | UEDOL | D10 |  |  | ORGINAL ESTIMATE DOLLARS |
| 17 | UERVD | D10 |  |  | REVISED ESTIMATE DOLLARS |
| 27 | UDTDR | D8 |  |  | DATE DOLLARS REVISED |
| 35 | UCURD | D10 |  |  | CURRENT PERIOD DOLLARS |
| 45 | UPTDD | D10 |  |  | PROJECT TO DATE DOLLARS |
| 55 | UEQTY | D10 |  |  | ORGINAL ESTIMATE QUANTITY |
| 65 | UERVQ | D10 |  |  | REVISED ESTIMATE QUANTITY |
| 75 | UDTQR | D8 |  |  | DATE QUANTITY REVISED |
| 83 | UCURQ | D10 |  |  | ACTUAL QUANTITY CURRENT PERIOD |
| 93 | UPTDQ | D10 |  |  | ACTUAL QUANTITY PROJECT TO DATE |
| 103 | UCOMP | A1 |  |  | PROJECT COMPLETE Y OR N |

### UMFCT - COMMON, computed 104 bytes

UNIT COST MASTER FILE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A84 |  |  |  |
| 84 | UMFSF | D1 |  |  | SORT FLAG |
| 85 | UMFDF | D1 |  |  | DELETE FLAG |
| 86 | UMFOC | D5 |  |  | ORGANIZED COUNT |
| 91 | UMFRC | D5 |  |  | RECORD COUNT |
| 96 | UMFMX | D5 |  |  | MAXIMUM RECORD COUNT |
| 101 | UMFDC | D3 |  |  | DELETE COUNT |

## UNTTF.FD

### UNTTF - RECORD, declared A65, computed 65

UNIT COST TRANSACTION FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | UTUNT | D7 |  |  | UNIT COST NUMBER |
| 7 | UTGLA | D7 |  |  | G/L ACCOUNT NUMBER |
| 14 | UTDAT | D8 |  |  | TRX DATE |
| 22 | UTDSC | A30 |  |  | DESCRIPTION |
| 52 | UTAMT | D10 |  |  | TRX DOLLAR AMOUNT OR QUANTITY |
| 62 | UTSRC | A2 |  |  | SOURCE OF TRANSACTION |
| 64 | UTCOD | A1 |  |  | CODE (A = AMOUNT, Q = QUANTITY) |

### UTFCT - RECORD, computed 65 bytes

UNIT COST TRANSACTION FILE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A52 |  |  |  |
| 52 | UTFRC | D5 |  |  | RECORD COUNT |
| 57 | UTFMX | D5 |  |  | MAXIMUM RECORD COUNT |
| 62 | *(filler)* | A3 |  |  |  |

## UNTTF.FDC

### UNTTF - COMMON, declared A65, computed 65

UNIT COST TRANSACTION FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | UTUNT | D7 |  |  | UNIT COST NUMBER |
| 7 | UTGLA | D7 |  |  | G/L ACCOUNT NUMBER |
| 14 | UTDAT | D8 |  |  | TRX DATE |
| 22 | UTDSC | A30 |  |  | DESCRIPTION |
| 52 | UTAMT | D10 |  |  | TRX DOLLAR AMOUNT OR QUANTITY |
| 62 | UTSRC | A2 |  |  | SOURCE OF TRANSACTION |
| 64 | UTCOD | A1 |  |  | CODE (A = AMOUNT, Q = QUANTITY) |

### UTFCT - COMMON, computed 65 bytes

UNIT COST TRANSACTION FILE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A52 |  |  |  |
| 52 | UTFRC | D5 |  |  | RECORD COUNT |
| 57 | UTFMX | D5 |  |  | MAXIMUM RECORD COUNT |
| 62 | *(filler)* | A3 |  |  |  |

## VENIX.FD

### VENIX - RECORD, declared A8, computed 8

VENDOR MASTER INDEX (VENIX.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | VIVND | D4 | D4 |  | VENDOR NUMBER |
| 4 | VIREC | D4 | D4 |  | RECORD NUMBER IN VENDOR MASTER |

### (overlay 1) - RECORD, computed 4 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | VIVN2 | A4 |  |  | ALPHA VENDOR NUMBER |

## VENIX.FDC

### VENIX - COMMON, declared A8, computed 8

VENDOR MASTER INDEX (VENIX.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | VIVND | D4 | D4 |  | VENDOR NUMBER |
| 4 | VIREC | D4 | D4 |  | RECORD NUMBER IN VENDOR MASTER |

### (overlay 1) - COMMON, computed 4 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | VIVN2 | A4 |  |  | ALPHA VENDOR NUMBER |

## VENMS.FD

### VENMS - RECORD, declared A173, computed 173

VENDOR MASTER FILE (VENMS.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | VMVND | D4 | D4 |  | VENDOR NUMBER |
| 4 | VMNAM | A25 | A25 |  | VENDOR NAME |
| 29 | VMAD1 | A25 | A25 |  | ADDRESS LINE 1 |
| 54 | VMAD2 | A25 | A25 |  | ADDRESS LINE 2 |
| 79 | VMCTY | A15 | A15 |  | CITY |
| 94 | VMSTA | A2 | A2 |  | STATE |
| 96 | VMZIP | A9 | A9 |  | ZIP CODE |
| 105 | VMAMT | D10 | D10.2 |  | AMOUNT BILLED YTD |
| 115 | VMVCH | D4 | D4 |  | NUMBER OF VOUCHERS YTD |
| 119 | VMPAY | A8 | A8 |  | METHOD OF PAYMENT |
| 127 | VMNUM | A1 | A1 |  | S=SS#, F=FID#, BLANK |
| 128 | VMSFN | D9 | D9 |  | SS# OR FID# |
| 137 | VMMNO | D10 | D10 |  | MISCELLANEOUS NUMBER |
| 147 | VMTYP | A2 | A2 |  | 1099 TYPE |
| 149 | VMYTD | D10 | D10.2 |  | PAID OUT YTD |
| 159 | VMSUM | A1 | A1 |  | Y=PRINT SUMMARY CK STUB |
| 160 | VMTRM | D3 | D3.1 |  | TERMS |
| 163 | VMACD | D3 | D3 |  | AREA CODE |
| 166 | VMPHN | D7 | D7 |  | PHONE NUMBER |

### VMCTL - RECORD, computed 173 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A153 |  |  |  |
| 153 | VMDFG | D1 |  |  | DELETE FLAG |
| 154 | VMSFG | D1 |  |  | SORT FLAG |
| 155 | VMORG | D5 |  |  | ORGANIZE COUNT |
| 160 | VMREC | D5 |  |  | RECORD COUNT |
| 165 | VMMAX | D5 |  |  | MAXIMUM COUNT |
| 170 | VMDEL | D3 |  |  | DELETE COUNT |

## VENMS.FDC

### VENMS - COMMON, declared A173, computed 173

VENDOR MASTER FILE (VENMS.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | VMVND | D4 | D4 |  | VENDOR NUMBER |
| 4 | VMNAM | A25 | A25 |  | VENDOR NAME |
| 29 | VMAD1 | A25 | A25 |  | ADDRESS LINE 1 |
| 54 | VMAD2 | A25 | A25 |  | ADDRESS LINE 2 |
| 79 | VMCTY | A15 | A15 |  | CITY |
| 94 | VMSTA | A2 | A2 |  | STATE |
| 96 | VMZIP | A9 | A9 |  | ZIP CODE |
| 105 | VMAMT | D10 | D10.2 |  | AMOUNT BILLED YTD |
| 115 | VMVCH | D4 | D4 |  | NUMBER OF VOUCHERS YTD |
| 119 | VMPAY | A8 | A8 |  | METHOD OF PAYMENT |
| 127 | VMNUM | A1 | A1 |  | S=SS#, F=FID#, BLANK |
| 128 | VMSFN | D9 | D9 |  | SS# OR FID# |
| 137 | VMMNO | D10 | D10 |  | MISCELLANEOUS NUMBER |
| 147 | VMTYP | A2 | A2 |  | 1099 TYPE |
| 149 | VMYTD | D10 | D10.2 |  | PAID OUT YTD |
| 159 | VMSUM | A1 | A1 |  | Y=PRINT SUMMARY CK STUB |
| 160 | VMTRM | D3 | D3.1 |  | TERMS |
| 163 | VMACD | D3 | D3 |  | AREA CODE |
| 166 | VMPHN | D7 | D7 |  | PHONE NUMBER |

### VMCTL - COMMON, computed 173 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A153 |  |  |  |
| 153 | VMDFG | D1 |  |  | DELETE FLAG |
| 154 | VMSFG | D1 |  |  | SORT FLAG |
| 155 | VMORG | D5 |  |  | ORGANIZE COUNT |
| 160 | VMREC | D5 |  |  | RECORD COUNT |
| 165 | VMMAX | D5 |  |  | MAXIMUM COUNT |
| 170 | VMDEL | D3 |  |  | DELETE COUNT |

## VENNX.FD

### VENNX - RECORD, declared A33, computed 33

VENDOR NAME INDEX FILE (VENNX.FDC)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | VNNAM | A25 | A25 |  | VENDOR NAME |
| 25 | VNVND | D4 | D4 |  | VENDOR NUMBER |
| 29 | VNREC | D4 | D4 |  | RECORD NBR IN VENDOR MASTER |

### (overlay 1) - RECORD, computed 29 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | VNKEY | A29 |  |  | VENDOR NAME - VENDOR NUMBER |

## VENNX.FDC

### VENNX - COMMON, declared A33, computed 33

VENDOR NAME INDEX FILE (VENNX.FDC)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | VNNAM | A25 | A25 |  | VENDOR NAME |
| 25 | VNVND | D4 | D4 |  | VENDOR NUMBER |
| 29 | VNREC | D4 | D4 |  | RECORD NBR IN VENDOR MASTER |

### (overlay 1) - COMMON, computed 29 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | VNKEY | A29 |  |  | VENDOR NAME - VENDOR NUMBER |

## XCASH.FD

### XCASH - RECORD, declared A80, computed 80

CASH RECEIPTS FILE (XCASH.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | CXCNO | A5 | A5 |  | CUSTOMER NUMBER |
| 5 | CXCNM | A25 | A25 |  | CUSTOMER NAME |
| 30 | CXRDT | D8 | D8 |  | RECEIPT DATE |
| 38 | CXCKN | D6 | D6 |  | CHECK NUMBER |
| 44 | CXAMT | D8 | D8 |  | AMOUNT RECEIVED |
| 52 | CXDIS | D7 | D7 |  | DISCOUNT AMOUNT |
| 59 | CXAPL | D6 | D6 |  | APPLY TO NUMBER |
| 65 | CXMSC | D8 | D8 |  | MISC AMOUNT |
| 73 | CXGLA | D7 | D7 |  | GENERAL LEDGER NUMBER |

### CXCTL - RECORD, computed 80 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A62 |  |  |  |
| 62 | CXORG | D5 |  |  | ORGANIZE COUNT |
| 67 | CXREC | D5 |  |  | RECORD COUNT |
| 72 | CXMAX | D5 |  |  | MAXIMUM COUNT |
| 77 | CXDEL | D3 |  |  | DELETE COUNT |

## YTD1F.FD

### YTD1F - RECORD, declared A147, computed 147

TEMPORARY G/L YTD TRX FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | Y1ACT | D7 | D7 |  | ACCOUNT NUMBER |
| 7 | Y1BAL | 14D10 | A140 |  | BAL PER PERIOD OR YTD AND GRAND TOTAL |

### Y1CTL - RECORD, computed 147 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A116 |  |  |  |
| 116 | Y1SPD | D2 |  |  | STARTING PERIOD |
| 118 | Y1EPD | D2 |  |  | ENDING PERIOD |
| 120 | Y1SDT | D8 |  |  | STARTING DATE |
| 128 | Y1EDT | D8 |  |  | ENDING DATE |
| 136 | Y1PFC | D3 |  |  | PROFIT CENTER |
| 139 | Y1BSF | D1 |  |  | BALANCE SHEET FLAG (1=PRINT) |
| 140 | Y1SSF | D1 |  |  | SUPPORTING SHEDULE FLAG (1=PRINT) |
| 141 | Y1RAT | D1 |  |  | PRINT WITH RATIOS (1=PRINT) |
| 142 | Y1REC | D5 |  |  | # OF RECORDS FILE |

## YTDCC.FD

### YTDCC - RECORD, declared A638, computed 638

CUSTOMER CATEGORY SALES FILE (YTDCC.FD)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | YCCNO | A5 | A5 |  | CUSTOMER NUMBER |
| 5 | YCSLS | D2 | D2 |  | SALESMAN NUMBER |
| 7 | YCEXS | 30D7 | A210 |  | SALES |
| 217 | YCEXC | 30D7 | A210 |  | COST |
| 427 | YCEXQ | 30D7 | A210 |  | QUANTITY |
| 637 | YCDFG | A1 | A1 |  | DELETE FLAG |

### YCCTL - RECORD, computed 638 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A620 |  |  |  |
| 620 | YCORG | D5 |  |  | ORGANIZE COUNT |
| 625 | YCREC | D5 |  |  | RECORD COUNT |
| 630 | YCMAX | D5 |  |  | MAXIMUM COUNT |
| 635 | YCDEL | D3 |  |  | DELETE COUNT |

## YTDCC.FDC

### YTDCC - COMMON, declared A638, computed 638

CUSTOMER CATEGORY SALES FILE (YTDCC.FDC)

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | YCCNO | A5 | A5 |  | CUSTOMER NUMBER |
| 5 | YCSLS | D2 | D2 |  | SALESMAN NUMBER |
| 7 | YCEXS | 30D7 | A210 |  | SALES |
| 217 | YCEXC | 30D7 | A210 |  | COST |
| 427 | YCEXQ | 30D7 | A210 |  | QUANTITY |
| 637 | YCDFG | A1 | A1 |  | DELETE FLAG |

### YCCTL - COMMON, computed 638 bytes

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A620 |  |  |  |
| 620 | YCORG | D5 |  |  | ORGANIZE COUNT |
| 625 | YCREC | D5 |  |  | RECORD COUNT |
| 630 | YCMAX | D5 |  |  | MAXIMUM COUNT |
| 635 | YCDEL | D3 |  |  | DELETE COUNT |

## YTDGL.FD

### YTDGL - RECORD, declared A58, computed 58

YTD G/L TRX FILE

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | YGACT | D7 | D7 |  | G/L ACCOUNT NUMBER |
| 7 | YGDAT | D8 | D8 |  | TRANSACTION DATE |
| 15 | YGAMT | D10 | D10.2 |  | TRANSACTION AMOUNT |
| 25 | YGSRC | A3 | A3 |  | TRANSACTION SOURCE |
| 28 | YGREF | A30 | A30 |  | TRANSACTION REFERENCE |

### YGCTL - RECORD, computed 58 bytes

YTD G/L TRX FILE CONTROL RECORD

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | *(filler)* | A3 |  |  |  |
| 3 | YGSPD | D2 | D2 |  | STARTING PERIOD NUMBER |
| 5 | YGEPD | D2 | D2 |  | ENDING PERIOD NUMBER |
| 7 | YGSDT | D8 | D8 |  | STARTING PERIOD DATE |
| 15 | YGEDT | D8 | D8 |  | ENDING PERIOD DATE |
| 23 | YGPFC | D3 | A3 |  | PROFIT CENTER |
| 26 | YGCFG | D1 |  |  | FLAG (1=BUDGETS,3=COMPARATIVES)D1 |
| 27 | YGBSF | D1 | D1 |  | BALANCE SHEET FLAG (1=PRINT) |
| 28 | YGSSF | D1 | D1 |  | SUPP SCHEDULE FLAG (1=PRINT) |
| 29 | YGRDT | D8 | D8 |  | REPORT DATE |
| 37 | *(filler)* | A3 |  |  |  |
| 40 | YGORG | D5 | D5 |  | ORGANIZED COUNT |
| 45 | YGREC | D5 | D5 |  | RECORD COUNT |
| 50 | YGMAX | D5 | D5 |  | MAXIMUM # OF RECORDS |
| 55 | *(filler)* | A3 |  |  |  |

## YTDIX.FD

### YTDIX - RECORD, declared A23, computed 23

FINANCIAL STATEMENT INDEX

| Off | Field | Type | Prec | Init | Description |
|---|---|---|---|---|---|
| 0 | YIACT | D7 | D7 |  | G/L ACCOUNT NUMBER |
| 7 | YIFSC | A7 | A7 |  | FINANCIAL STATEMENT CODE |
| 14 | YIMAS | D4 | D4 |  | RECORD # IN G/L ACCOUNT MASTER |
| 18 | YIREC | D5 | D5 |  | REC # OF 1ST TRX IN YTDGL FILE |

---

160 files, 339 records, 2425 fields.
