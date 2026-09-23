@ECHO OFF
REM Start the accounting system. Double-click, or run from a Command Prompt.
REM 132 columns so reports sent to the screen (TT:) fit, as on the VT100.
CALL "%~dp0ENV.BAT"
MODE CON: COLS=132 LINES=25 > NUL 2>&1
python "%~dp0term.py" SY:IDCTRL
ECHO.
PAUSE
