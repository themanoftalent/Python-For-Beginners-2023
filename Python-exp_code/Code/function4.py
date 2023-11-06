#! /usr/bin/python
# Filename : function4.py
# Description: when using global, we mean to use parameters which are
# defined outside, so changes will remain after function excute. 

def funcWithGlobalParameter():
    global x 
    print 'x is', x
    x = 2

x = 50
funcWithGlobalParameter()
print 'now x is',x
