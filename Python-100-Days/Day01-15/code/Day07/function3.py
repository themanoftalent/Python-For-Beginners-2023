
#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

is local, so the changes cannot effect the outside variable.

def funcGlobal(x):
    print 'x is', x
    x = 2 #define the local varible x
    print 'x value changes to', x

x = 50
funcGlobal(x)
