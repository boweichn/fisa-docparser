import pyodbc
import os


# for row in db_object:
#     print (row)

def return_db_object():
    
    db_file = 'test.accdb'
    file_path = os.path.abspath(db_file)
    
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s'%file_path)
    cursor = conn.cursor()
    cursor.execute('select * from Table1')

    db_object = cursor.fetchall()
    return db_object
