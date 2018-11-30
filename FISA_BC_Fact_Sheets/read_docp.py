import json
import csv
import requests
from pprint import pprint


def json_to_dict():
    x = json.loads(requests.get('https://api.docparser.com/v1/results/jdoaqgsovumx?api_key=832da014350ae9eddd8bec41a2ccc141f7da93b1').content)

    my_dict_list = []
    my_temp_dict = {}
    
    for i in x:
        my_temp_dict = {
            i["school_num"]:
                {
                    "school".upper(): i["school"] if i["school"] != None else True,
                    "address".upper(): i["address"] if i["address"] != None else True,
                    "saddress".upper(): i["saddress"] if i["saddress"] != None else True,
                    "founded".upper(): i["founded"] if i["founded"] != None else True,
                    "phone".upper(): i["phone"] if i["phone"] != None else True,
                    "fax".upper(): i["fax"] if i["fax"] != None else True,
                    "Website": i["website"] if i["website"] != None else True,
                    "Email": i["email"] if i["email"] != None else True,
                    "city".upper(): i["city"] if i["city"] != None else True,
                    "postal".upper(): i["postal"] if i["postal"] != None else True,
                    "grades".upper(): i["grades"] if i["grades"] != None else True,
                    "funding".upper(): i["funding"] if i["funding"] != None else True,
                    "specialty".upper(): i["specialty"] if i["specialty"] != None else True,
                    "fisa".upper(): i["fisa"] if i["fisa"] != None else True,
                    "assoc".upper(): i["assoc"] if i["assoc"] != None else True,
                    "assoc2".upper(): i["assoc2"] if i["assoc2"] != None else True,
                    "sdnum".upper(): i["sdnum"] if i["sdnum"] != None else True,
                    "sd".upper(): i["sd"] if i["sd"] != None else True,
                    "electoral".upper(): i["electoral2"] if i["electoral2"] != None else True,
                    "Halfday_k": i["halfday_k"] if i["halfday_k"] != None else True,
                    "Fullday_k": i["fullday_k"] if i["fullday_k"] != None else True,
                    "1_7": i["1_7"] if i["1_7"] != None else True,
                    "une".upper(): i["une"] if i["une"] != None else True,
                    "8": i["key_8"] if i["key_8"] != None else True,
                    "9": i["key_9"] if i["key_9"] != None else True,
                    "10": i["key_10"] if i["key_10"] != None else True,
                    "11": i["key_11"] if i["key_11"] != None else True,
                    "12": i["key_12"] if i["key_12"] != None else True,
                    "uns".upper(): i["uns"] if i["uns"] != None else True,
                    "last".upper(): i["last"] if i["last"] != None else True,
                    "first".upper(): i["first"] if i["first"] != None else True,
                    "degree".upper(): i["degree"] if i["degree"] != None else True
                }
            
            
        }
        my_dict_list.append(my_temp_dict)
    
    return my_dict_list

if __name__ == "__main__":
    pprint(json_to_dict())