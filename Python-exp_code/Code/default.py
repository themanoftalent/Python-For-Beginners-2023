#! /usr/bin/python
# Filename: default.py
# Description: default parameter demos

def func(message, times = 1):
    print 'message', message
    print 'times', times

x = "this is first parameters"
func(x) ## Note, here we use only one paramters

y = 5
func(x, y) # Here we use two paramters which meets the declaration.
