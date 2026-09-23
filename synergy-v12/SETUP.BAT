@ECHO OFF
REM Build a fresh, empty test installation: runtime files in WORK\,
REM company data in DAT\001-005\. Both are outside git. Refuses to run
REM over an existing installation unless given /FRESH.

SETLOCAL
CALL "%~dp0ENV.BAT"
IF EXIST "%ACCROOT%\WORK\COFILE.DDF" IF /I NOT "%1"=="/FRESH" (
  ECHO WORK\COFILE.DDF already exists. Run SETUP /FRESH to wipe WORK\ and DAT\.
  EXIT /B 1
)

IF EXIST "%ACCROOT%\WORK" RMDIR /S /Q "%ACCROOT%\WORK"
IF EXIST "%ACCROOT%\DAT" RMDIR /S /Q "%ACCROOT%\DAT"
FOR %%D IN (WORK DAT DAT\001 DAT\002 DAT\003 DAT\004 DAT\005 SPL BCK) DO IF NOT EXIST "%ACCROOT%\%%D" MKDIR "%ACCROOT%\%%D"

XCOPY /Q /Y "%ACCROOT%\RUN\*.*" "%ACCROOT%\WORK\" > NUL
COPY /Y "%ACCROOT%\V12\SECPROGS.TXT" "%ACCROOT%\WORK\" > NUL

CD /D "%ACCROOT%\V12"
dbl NEWCO.DBL || EXIT /B 1
dblink NEWCO.DBO || EXIT /B 1
CD /D "%ACCROOT%\WORK"
dbr "%ACCROOT%\V12\NEWCO.DBR" < NUL
DEL SECPROGS.TXT
python "%ACCROOT%\V12\newco_init.py" || EXIT /B 1
ENDLOCAL
