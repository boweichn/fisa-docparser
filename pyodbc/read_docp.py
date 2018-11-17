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
                    "school".upper(): i["school"],
                    "address".upper(): i["address"],
                    "saddress".upper(): i["saddress"],
                    "founded".upper(): i["founded"],
                    "phone".upper(): i["phone"],
                    "fax".upper(): i["fax"],
                    "Website": i["website"],
                    "Email": i["email"],
                    "city".upper(): i["city"],
                    "postal".upper(): i["postal"],
                    "grades".upper(): i["grades"],
                    "funding".upper(): i["funding"],
                    "specialty".upper(): i["specialty"],
                    "fisa".upper(): i["fisa"],
                    "assoc".upper(): i["assoc"],
                    "other".upper(): i["other"],
                    "sdnum".upper(): i["sdnum"],
                    "sd".upper(): i["sd"],
                    "electoral".upper(): i["electoral2"],
                    "Halfday_k": i["halfday_k"] if i["key_8"] != None else 0,
                    "Fullday_k": i["fullday_k"] if i["key_8"] != None else 0,
                    "1_7": i["1_7"] if i["key_8"] != None else 0,
                    "une".upper(): i["une"] if i["key_8"] != None else 0,
                    "8": i["key_8"] if i["key_8"] != None else 0,
                    "9": i["key_9"] if i["key_8"] != None else 0,
                    "10": i["key_10"] if i["key_8"] != None else 0,
                    "11": i["key_11"] if i["key_8"] != None else 0,
                    "12": i["key_12"] if i["key_8"] != None else 0,
                    "uns".upper(): i["uns"] if i["key_8"] != None else 0
                }
            
            
        }
        my_dict_list.append(my_temp_dict)
    
    return my_dict_list

if __name__ == "__main__":
    pprint(json_to_dict())