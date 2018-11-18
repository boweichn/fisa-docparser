mode con:cols=150 lines=50
@ECHO OFF
TITLE Email PDF Files To Schools

ECHO Executing Production Batch...
ECHO Emailing PDF Files...
ECHO.
ECHO ******************************************************

"C:\Program Files (x86)\Python37-32\python.exe" "email_pdf.py"

ECHO.
ECHO ******************************************************

ECHO.
ECHO All PDF files have been emailed.
ECHO.
PAUSE
