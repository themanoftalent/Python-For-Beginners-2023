import re
mailAddress='guru99@google.com, careerguru99@hotmail.com , users@yahoomail.com'

emails=re.findall(r'[\w\.-]+@[\w\.-]+',mailAddress)

print('Printing all emails')
for mail in emails:
    print(emails)