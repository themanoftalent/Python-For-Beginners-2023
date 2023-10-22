import csv



with open('sozcu.csv', 'r') as d:
    r = csv.DictReader(d)
    for rows in r:
        print(rows['firstname'])


'''
with open('sozcu.csv', 'w') as dictf:
    f = ['firstname', 'lastname']
    wd = csv.DictWriter(dictf, fieldnames=f)
    wd.writeheader()
    wd.writerow({'firstname':'canan', 'lastname':'kaya'})
    wd.writerow({'firstname':'ali', 'lastname':'demir'})
    wd.writerow({'firstname':'murat', 'lastname':'salim'})
'''
