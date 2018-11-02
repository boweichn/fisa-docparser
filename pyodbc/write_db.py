import pyodbc
import os
from read_db import return_db_object
from csv_obj import read_csv

def write_to_db(my_data):
  db_file = 'test.accdb'
  file_path = os.path.abspath(db_file)

  conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s'%file_path)
  cursor = conn.cursor()

  my_csv = my_data

  for rows in my_csv:
    if (rows[1] != ''):
      cursor.execute('''
                     UPDATE Table1
                     SET Key = {}
                     WHERE ID = {}
                   
                    '''.format(rows[1], rows[0]))
      conn.commit()