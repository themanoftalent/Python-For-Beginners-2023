
#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

#here we equal them
# new_listem = old_listem

#we could use copy 
# You can see that, the old list remains unchanged even when the new list is modified.


old_listem = [1, 2, 3,4,5,6,7,8]
new_listem=old_listem.copy()

# add element to list
new_listem.append('a')
new_listem.append('b')

new_listem.append('c')
new_listem.append('d')
new_listem.append('son')

print('New List:', new_listem )
print('Old List:', old_listem )