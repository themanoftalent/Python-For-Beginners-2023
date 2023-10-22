##################################################
#### **************************************** ####
#### !/usr/bin/python3                        ####
#### -*- coding: utf-8 -*-                    ####
#### @Time    : 2023/20/10 11:40              ####
#### @Author  : themanoftalent                ####
#### @Site:https://github.com/themanoftalent  ####
#### @Project : python-app                    ####
#### **************************************** ####
##################################################
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

