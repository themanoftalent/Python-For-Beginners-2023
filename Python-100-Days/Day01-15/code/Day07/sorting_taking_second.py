#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

# take second element for sort
def takeSecond(elem):
    return elem[1]

# random list
random = [(2, 2),(7,9), (3, 4),(5,0), (4, 1), (1, 3),(6,5),(2, 6),(7,11), (3, 14),(5,10), (4, 21), (1, 13),(6,15)]

# sort list with key
random.sort(key=takeSecond)


# print list
print('Sorted list:', random)


#calling method
takeSecond('calling methods')