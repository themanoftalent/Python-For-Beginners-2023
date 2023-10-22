#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

letsets={'hello'}
print(type(letsets))
letsets.add('This is ')

print(dir(letsets))

letsets.add('No where is ')
letsets.add(None)
letsets.add(123214)

print(letsets.pop())

print(letsets.pop())
print(letsets)