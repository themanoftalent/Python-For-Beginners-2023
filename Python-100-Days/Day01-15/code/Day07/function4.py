
#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.

def funcWithGlobalParameter():
    global x 
    print 'x is', x
    x = 2

x = 50
funcWithGlobalParameter()
print 'now x is',x
