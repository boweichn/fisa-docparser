import pyodbc
import os
from read_docp import json_to_dict
from colorama import init
from termcolor import colored
from pprint import pprint

def write_to_db(my_data):

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
  for rows in my_data:
    for key, value in rows.items():
      for fields, data in value.items():
        if fields in results[0].keys():
          altSQL = "UPDATE DBMAIN SET %s = ? WHERE SCHOOL_NUM = ?;"%(fields)
          cursor.execute(altSQL, (data, key))
          conn.commit()

  print(colored('All other field data are updated... \n', 'green'))