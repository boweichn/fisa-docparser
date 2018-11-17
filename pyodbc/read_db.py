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

def retrive_dict():

    # Input File
    db_file = 'schools.accdb'

    # Finding abspath for Input File
    file_path = os.path.abspath(db_file)

    # Engaging Access Drivers for fetch connecton
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s'%file_path)
    cursor = conn.cursor().execute("SELECT * FROM DBMAIN")
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))

    return results

if __name__ == "__main__":
    print(return_db_object())
