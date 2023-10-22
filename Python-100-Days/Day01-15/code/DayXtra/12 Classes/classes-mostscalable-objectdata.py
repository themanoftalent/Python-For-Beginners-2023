#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:

    # Or even better, store attributes in a dictionary as well.
    def __init__(self, **kwargs):
        # Default color to white
        self._attributes = kwargs

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def get_attribute(self, key):
        return self._attributes.get(key, None)

    def set_attribute(self, key, value):
        print("Changing attribute {} to {}: ".format(key, value))
        self._attributes[key] = value

def main():
    donald = Duck(color = 'blue')
    print(donald.get_attribute('color'))
    steve = Duck(color = 'red')
    print(steve.get_attribute('color'))
    steve.set_attribute('feet', 2)
    print(steve.get_attribute('feet'))
    # steve = Duck(color = 'red')
    # print(steve.get_color())

if __name__ == "__main__": main()
