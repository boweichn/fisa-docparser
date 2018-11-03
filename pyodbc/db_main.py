from write_db import write_to_db
from read_db import return_db_object
from read_docp import json_to_dict
import pyodbc

def main():

    print("\n")
    print("Returning input update data...")
    print(json_to_dict())
    write_to_db(json_to_dict())
    
main()