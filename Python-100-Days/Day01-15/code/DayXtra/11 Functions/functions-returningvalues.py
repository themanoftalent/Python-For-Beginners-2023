#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print(testfunc())
    print(testfuncNumber())
    print(testfuncRange())
    for n in testfuncRange():
        print(n, end = " ")

def testfunc():
    return 'This is a test function'

def testfuncNumber():
    return 42

def testfuncRange():
    return range(25)

if __name__ == "__main__": main()
