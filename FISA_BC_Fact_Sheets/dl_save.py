import requests
import os

for filename in os.listdir('./prepared_fact_sheets'):
    file_url = "file:///C:/Users/StephenCheng/Desktop/FISA_COLLAB/pyodbc/prepared_fact_sheets/%s"%(filename.replace(' ', '%'))
    
    r = requests.get(file_url, stream = True) 
    
    with open("./test_save/%s"%(filename),"wb") as pdf: 
        for chunk in r.iter_content(chunk_size=1024): 
    
            # writing one chunk at a time to pdf file 
            if chunk: 
                pdf.write(chunk) 