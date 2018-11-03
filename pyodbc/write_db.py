import pyodbc
import os
from read_docp import json_to_dict

def write_to_db(my_data):

  # Input File
  db_file = 'schools.accdb'

  # Finding abspath for Input File
  file_path = os.path.abspath(db_file)

  # Engaging Access Drivers for fetch connecton
  conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s'%file_path)
  cursor = conn.cursor()

  for rows in my_data:
    for key, value in rows.items():
      for fields, data in value.items():
        try:
          my_data = int(data)
          mySQL = "UPDATE DBMAIN SET %s = %s WHERE SCHOOL_NUM = '%s';"%(fields, my_data, key)
          print(mySQL)
          cursor.execute(mySQL)
          conn.commit()
        except:
          altSQL = "UPDATE DBMAIN SET %s = '%s' WHERE SCHOOL_NUM = '%s';"%(fields, data, key)
          print(altSQL)
          cursor.execute(altSQL)
          conn.commit()
