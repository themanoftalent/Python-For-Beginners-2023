#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

import re
mailAddress='ahmet@google.com, camelahmet@hotmail.com , sultan@yahoomail.com'

emails=re.findall(r'[\w\.-]+@[\w\.-]+',mailAddress)

print('Printing all emails')
for mail in emails:
    print(emails)