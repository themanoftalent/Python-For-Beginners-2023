#! /usr/bin/python
# Filename: dict.py
# Description: a simple demo to use dict

dic = { 'deercoder':'deercoder@gmail.com',
        'Emily': 'emily@gmail.com',
        'Frank': 'frank@gmail.com',
        'Stanley': 'stanley@gmail.com'
      }
print 'Stanley\'s email address is %s' % dic['Stanley']

### Now add a item
dic['kkpattern'] = 'kkpattern@gmail.com'
for name,address in dic.items():
    print 'Contact name is %s, address is %s' %(name, address)

del dic['Emily']
for name, address in dic.items():
    print 'Contact name is %s, address is %s' %(name, address)
