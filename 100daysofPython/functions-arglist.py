#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    testfunc(1,2,3)

# *args means optional arguments
def testfunc(arg1, *args):
    print(arg1, args)

if __name__ == "__main__": main()
