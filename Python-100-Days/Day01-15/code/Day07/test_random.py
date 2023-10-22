#!/usr/bin/env python

#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

import random

print random.random() # a random number from 0 to 1
print random.randrange(10) # interger random ends with 10
print random.randrange(1, 10) # start, end
print random.randrange(1, 10, 2) # start, end, step
print random.randint(1, 10) #  1<= N <= 10
print random.uniform(1.0, 10.0) # float random number
print random.choice(range(1, 10)) # select an sequence, any seq parameter
