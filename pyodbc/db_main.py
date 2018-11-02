from write_db import write_to_db
from read_db import return_db_object
from csv_obj import read_csv

def main():
    print("Reading Database")
    print("Returning Database....")
    print(return_db_object())
    write_to_db(read_csv())
    print("Updating Database with csv data...")
    print("Returning new Database...")
    print(return_db_object())

main()