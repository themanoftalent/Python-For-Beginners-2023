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

print random.random() # a random number from 0 to 1
print random.randrange(10) # interger random ends with 10
print random.randrange(1, 10) # start, end
print random.randrange(1, 10, 2) # start, end, step
print random.randint(1, 10) #  1<= N <= 10
print random.uniform(1.0, 10.0) # float random number
print random.choice(range(1, 10)) # select an sequence, any seq parameter
