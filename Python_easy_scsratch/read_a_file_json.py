#Dictionary - True/False, None, 1,2,3
#JSON - true/false, null, "1", "2"
# loads - takes string that is in the json format, and prints it in dictionary
# load - takes a JSON file, and converts it into dictionary for python
#
# dumps - Dictionary in the form of string and convert it into string of json
# dump - will be taking dictionary and convert it into a json file.

import json

def dosya_oku():
    with open('new.json', 'r') as bf:
        print(json.load(bf))



dosya_oku()


