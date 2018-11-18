mode con:cols=150 lines=50
@ECHO OFF
TITLE Update Access with Parsed Data

ECHO Executing Production Batch...
ECHO Executing Parsing for Read and Write...
ECHO Updating Database...
ECHO.
ECHO ******************************************************

"C:\Program Files (x86)\Python37-32\python.exe" "db_main.py"
rem"C:\Users\StephenCheng\AppData\Local\Programs\Python\Python36-32\python.exe" "db_main.py"

ECHO.
ECHO ******************************************************

ECHO.
ECHO Queries have finised. Database is updated.
PAUSE