
#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

def func_key(a, b = 5, c = 43):
    print 'a is', a
    print 'b is', b
    print 'c is', c

print 'Former situation which we use default location'
func_key(1, 3, 4);

print '### Now, we use a parameter name to define it'
func_key(c = 2, b = 23, a = 1)
func_key(4, c = 56) # when not using name, we use default location to give value
