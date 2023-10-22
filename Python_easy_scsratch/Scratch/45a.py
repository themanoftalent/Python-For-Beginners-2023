import json

a = {1:'raunak', 2:'joshi'}

with open('name.json', 'w') as wj:
	json.dump(a, wj)


print("Operation Successful")