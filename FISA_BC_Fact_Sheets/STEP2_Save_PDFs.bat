mode con:cols=150 lines=50

@ECHO OFF

cd prepared_fact_sheets
for %%f in (*.*) do (
    echo Opening %%f ...
    start "" "%%f"
    timeout 3 > nul
    cd ..
    start "" "save_pdf.ahk"
    timeout 10 > nul
    cd prepared_fact_sheets
)

PAUSE