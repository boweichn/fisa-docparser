mode con:cols=300 lines=75
@ECHO OFF
TITLE This is a test batch for FISABC

ECHO Executing Production Test Batch...
ECHO Executing Parsing for Read and Write...
ECHO.
ECHO ******************************************************

"C:\Program Files (x86)\Python37-32\python.exe" "db_main.py"

ECHO.
ECHO ******************************************************

ECHO.
ECHO Queries have finised. Database is updated.
PAUSE