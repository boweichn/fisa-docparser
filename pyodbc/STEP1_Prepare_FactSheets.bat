mode con:cols=150 lines=50
@ECHO OFF
TITLE Fill Blank PDF with Data

ECHO Executing Production Batch...
ECHO Filling Empty Batch PDFs With Data...
ECHO.
ECHO ******************************************************

"C:\Program Files (x86)\Python37-32\python.exe" "pdf_filler.py"
rem"C:\Users\StephenCheng\AppData\Local\Programs\Python\Python36-32\python.exe" "pdf_filler.py"

ECHO.
ECHO ******************************************************

ECHO.
ECHO ALL BLANK PDFs HAS BEEN FILLED. PLEASE CHECK THE prepared_fact_sheets FOLDER WITHIN THE PDFs FOLDER
ECHO.
PAUSE