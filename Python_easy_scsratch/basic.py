import json

def abc():
    with open('new.json', 'r') as r:
        print(json.load(r))
