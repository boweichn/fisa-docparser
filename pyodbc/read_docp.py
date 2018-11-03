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
                    "Active": i["active"],
                    "93_94".upper(): i["93_94"],
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
                    "Halfday_k": i["halfday_k"],
                    "Fullday_k": i["fullday_k"],
                    "1_7": i["1_7"],
                    "une".upper(): i["une"],
                    "8": i["key_8"],
                    "9": i["key_9"],
                    "10": i["key_10"],
                    "11": i["key_11"],
                    "12": i["key_12"],
                    "uns".upper(): i["uns"]
                }
            
            
        }
        my_dict_list.append(my_temp_dict)
    
    return my_dict_list