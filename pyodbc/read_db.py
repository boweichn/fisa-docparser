import pyodbc
import os

def return_db_object():
    
    # Input file
    db_file = 'schools.accdb'

    # finding abspath of Input file
    file_path = os.path.abspath(db_file)
    
    # engaging Access driver and connect to input accdb file.
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s'%file_path)
    cursor = conn.cursor()
    cursor.execute('select * from dbmain')

    # fetch data
    db_object = cursor.fetchall()
    return db_object

if __name__ == "__main__":
    print(return_db_object())
