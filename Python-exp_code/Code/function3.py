#! /usr/bin/python
# Filename: function3.py
# Description: when changes the value in function, we use parameter which
# is local, so the changes cannot effect the outside variable.

def funcGlobal(x):
    print 'x is', x
    x = 2 #define the local varible x
    print 'x value changes to', x

x = 50
funcGlobal(x)
