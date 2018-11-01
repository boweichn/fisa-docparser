import pyodbc
import os

db_file = 'test.accdb'
file_path = os.path.abspath(db_file)

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s'%file_path)
cursor = conn.cursor()

  
# cursor.execute('''
#                     INSERT INTO table1 (ID, Key)
#                     VALUES(2, 200)

#                   ''')

cursor.execute('''
                    UPDATE table1
                    SET Key = 300
                    WHERE ID = 2
                    
                  ''')  

conn.commit()