from write_db import write_to_db
from read_db import return_db_object
from read_docp import json_to_dict
from compare import compareData
import pyodbc

def main():
    compareData()

    print('......\n')
    print('......\n')
    
    write_to_db(json_to_dict())
    
main()