#  !/usr/bin/python
#  Copyright (c) akifciftci 2019. Aim to help new beginner to try hard and learn more.
#

import random

print(random.randrange(1, 20))
print('==============================')

x = ['a', 'b', 'c', 'd', 'e']
print(random.choice(x))
print('**********'*3)
random.shuffle(x)
print(x)

print('==============================')
print('One to zero')
print(random.random())
print('==============================')
print('One to two thousands')
print(random.randint(1,2000))
print('==============================')
print('One to hundred')
print(random.randrange(100))

print('==============================')

