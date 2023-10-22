#! /usr/bin/python

#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#


def printMax(x, y):
    '''Print the max number of input.
    
        The two values must be intergers.'''
    x = int(x)
    y = int(y)
    if x > y:
        print 'max is ', x
    else:   
        print 'max is ', y

printMax(56, 78)
print printMax.__doc__
print help(printMax)
