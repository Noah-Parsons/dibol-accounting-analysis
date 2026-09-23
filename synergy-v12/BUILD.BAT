@ECHO OFF
REM Build everything with Synergy/DE v12: XC.OLB, then each subsystem.
REM The original MAKxx.BAT scripts are run unchanged apart from their
REM hard-coded SET FD= line. Output goes to V12\BUILD.LOG.

SETLOCAL
CALL "%~dp0ENV.BAT"
SET LOG=%ACCROOT%\V12\BUILD.LOG
FOR %%D IN (DBL EXC EXC\AP EXC\AR EXC\BR EXC\GL EXC\PR EXC\SC EXC\SY) DO IF NOT EXIST "%ACCROOT%\%%D" MKDIR "%ACCROOT%\%%D"
ECHO Build started %DATE% %TIME% > "%LOG%"

REM ---- XC shared library (MAKDES + MAKLIB) ----
CD /D "%ACCROOT%\SRC\XC"
ECHO ==== XC >> "%LOG%"
DEL /Q *.DBO XC.OLB 2>NUL
FOR %%F IN (*.DBL) DO dbl %%F < NUL >> "%LOG%" 2>&1
dbl -o TTSTS.DBO "%ACCROOT%\V12\TTSTS.DBL" < NUL >> "%LOG%" 2>&1
SET OBJS=
FOR %%F IN (*.DBO) DO CALL SET OBJS=%%OBJS%% %%F
dblibr -c "%DBL%XC.OLB" %OBJS% < NUL >> "%LOG%" 2>&1

REM ---- Subsystems ----
FOR %%S IN (SY SC AP AR BR GL PR) DO CALL :SUB %%S
ECHO Build finished %DATE% %TIME% >> "%LOG%"
ENDLOCAL
GOTO :EOF

:SUB
CD /D "%ACCROOT%\SRC\%1"
ECHO ==== %1 >> "%LOG%"
DEL /Q *.DBO *.DBR 2>NUL
findstr /V /B /I /C:"SET FD" MAK%1.BAT > "%TEMP%\V12MAK%1.BAT"
CALL "%TEMP%\V12MAK%1.BAT" < NUL >> "%LOG%" 2>&1
DEL "%TEMP%\V12MAK%1.BAT"
COPY /Y *.DBR "%ACCROOT%\EXC\%1\" > NUL 2>&1
GOTO :EOF
