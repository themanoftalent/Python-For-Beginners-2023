#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#
#

post={'Name':'Ahmet','Age':34,'Pofession':'Teacher','salary':34566}

print(post['Name'])
print(post.keys())
print(post.values())
print(post.items())
print('\n')
for lines  in post.items():
    print(lines)
print('--'*34)
try:
    print(post['Location'])

except:
    KeyError

    print('Not found')

if 'location' not in post.values():
    loc=post.get('location', 'Istanbul')
    print(loc)
else:
    print('all is done well')


print('--'*34)

for key in post.keys():
    value=post[key]
    print(key,'=',value)









