#! /usr/bin/python
# Filename: function5.py
# Description: This script is used to test whether the 
# function could be used before declaration.

# test(); ## This couldn't work because of undefined error.

def test():
    print 'This is a test function'
test() # This could work well.
