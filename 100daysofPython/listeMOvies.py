#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#


Listes = ['Movies', 'Music', 'Files', 'Documents', 'Pictures','Mallware','Moonlihgt']
mFiles=[]
for title in Listes:
    if title.startswith('M'):
        mFiles.append(title)
        print(mFiles)


#a short way again
print('============================')
lFile=[title for title in Listes if title.startswith('D')]
print(lFile)
print('-------------------------------------------------')
# sorting

# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
vowels.sort()

# print vowels
print('Sorted list:', vowels)


print('-------------------------------------------------')

Listes = ['Movies', 'Music', 'Files', 'Documents', 'Pictures','Mallware','Moonlihgt']
Listes.sort()
print(Listes)