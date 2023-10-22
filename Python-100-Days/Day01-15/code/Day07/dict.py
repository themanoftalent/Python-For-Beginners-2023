
#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#


dic = { 'derman':'derman@gmail.com',
        'Emily': 'emily@gmail.com',
        'Faruk': 'faruk@gmail.com',
        'Sultan': 'sultan@gmail.com'
      }
print( 'Sultan\'s email address is %s' % dic['Sultan'])

### Now add a item
dic['karacan'] = 'karacan@gmail.com'
for name,address in dic.items():
    print( 'Contact name is %s, address is %s' %(name, address))

del dic['Emily']
for name, address in dic.items():
    print ('Contact name is %s, address is %s' %(name, address))
