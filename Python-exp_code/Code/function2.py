#! /usr/bin/python
# Filename: function2.py
# Description: This script is used to test function with parameters.

def funcWithParameter(a, b):
    if a > b:
        print 'max number is a =', a
    elif a < b:
        print 'max number is b=', b
    else:
        print 'equal'

x = 4
y = 8
funcWithParameter(x,y)
