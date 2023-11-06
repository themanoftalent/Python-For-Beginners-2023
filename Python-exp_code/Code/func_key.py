#! /usr/bin/python
# Filename: func_key.py
# Description: use parameter name to give value to parameters
# in former situtation, we give value with sequence so that 
# they are correspond to each other

def func_key(a, b = 5, c = 43):
    print 'a is', a
    print 'b is', b
    print 'c is', c

print 'Former situation which we use default location'
func_key(1, 3, 4);

print '### Now, we use a parameter name to define it'
func_key(c = 2, b = 23, a = 1)
func_key(4, c = 56) # when not using name, we use default location to give value
