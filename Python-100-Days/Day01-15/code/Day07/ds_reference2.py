#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#


print("Go shopping and buy the list below.\n")
sholist=["Apple","Onion","Carrot","Mango","Eggs","Banana","Badminton"]

del sholist[0]
sholist.append("Leamon")

print(sholist)
print("--"*35)

#No difference between both as myList points shoplist.
myList=sholist[:]
print(myList)
