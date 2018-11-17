import pyodbc
import os
from read_docp import json_to_dict
from colorama import init
from termcolor import colored

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
          cursor.execute(mySQL)
          conn.commit()
        except:
          altSQL = "UPDATE DBMAIN SET %s = '%s' WHERE SCHOOL_NUM = '%s';"%(fields, data, key)
          cursor.execute(altSQL)
          conn.commit()

  print(colored('All other field data are updated... \n', 'green'))