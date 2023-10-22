#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

# Filename: mylist.py

mylist = ['apple', 'orange','banana' ]
print 'list length is', len(mylist)
print 'memory size is', mylist.__sizeof__()
mylist.sort()
print 'mylist is', mylist

print '### Now, print each elements\n'
for i in mylist:
    print i,
print '\n'

mylist.append('pear')
print '### After adding, the list is'
print 'mylist is now', mylist
for i in mylist:
    print i,
print '\n'

newlist = ['a', 'b', 'c']
mylist.__add__(newlist)
print 'mylist is now###', mylist
print 'newlist is now###', newlist
