#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:

    # Constructor defined as a method with name '__init__'
    def __init__(self, value):
        print('constructor')
        self._v = value

    def quack(self):
        print('Quaaack!', self._v)

    def walk(self):
        print('Walks like a duck.', self._v)

def main():
    donald = Duck(47)
    donald.quack()
    donald.walk()

    donald2 = Duck(50)
    donald2.quack()
    donald2.walk()

if __name__ == "__main__": main()
