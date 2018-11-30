from write_db import write_to_db
from read_db import return_db_object
from read_docp import json_to_dict
from pprint import pprint

from colorama import init
from termcolor import colored

import pyodbc
import csv

def compareData():

    init()

    dataList = return_db_object()
    dataDict = {}

    comparingList = []
    parsedData = json_to_dict()

    diffList = []

    for items in dataList:
        dataDict[items[0]] = {'SCHOOL': items[1], 'Email': items[2], 'FIRST': items[3], \
        'LAST': items[4], 'ADDRESS': items[5], 'CITY': items[6], 'POSTAL': items[7], \
        'ASSOC': items[8], 'AUTHORITY': items[9]}

    for lines in parsedData:
        for key,val in lines.items():
            if (key in dataDict.keys()):
                comparingList.append({key:dataDict[key]})

    for lines in parsedData:
        for okey,oval in lines.items():
            for ocol, orows in oval.items():
                for items in comparingList:
                    for key, val in items.items():
                        for col, rows in val.items():
                            if (key==okey) and (col==ocol) and (orows != rows):
                                diffList.append((oval['SCHOOL'], ocol, rows, orows))
                                print("School name: {}'s {} Column has a value that needs updating...   \
                                \nThe old value of {} will now be replaced with the parsed data: {}...\n".format(colored(oval['SCHOOL'], 'green'), 
                                colored(ocol, 'green'), colored(rows, 'green'), colored(orows, 'green')))

    if diffList == []:
        print(colored("No changes to any School's Email, Principals, or School Names.\n", 'green'))
    else:
        write_diff_to_csv(diffList)
        print('Changes to these data can be viewed in the file: {} in the {}.'.format(colored('recent_update_changes.csv', 'green'), colored('Updated_Data_Logs Folder', 'green')))
    return diffList

def write_diff_to_csv(my_list):
    with open('./Updated_Data_logs/recent_update_changes.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        header = ['SCHOOL_NAME', 'COLUMN_NAME', 'OLD_DATA', 'NEW_DATA']
        csv_writer.writerow(header)
        for datarow in my_list:
            csv_writer.writerow(datarow)        
    return

if __name__ == "__main__":
    compareData()