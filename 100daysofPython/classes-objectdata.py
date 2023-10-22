#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:
    # We can use simple arguments for constructors
    # def __init__(self, color = "white"):
    #     self._color = color

    # Or keyword arguments for constructors for scaling to multiple arguments
    # def __init__(self, **kwargs):
    #     # Default color to white
    #     self._color = kwargs.get('color', 'white')

    # Or even better, store attributes in a dictionary as well.
    def __init__(self, **kwargs):
        # Default color to white
        self._attributes = kwargs


    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    # def get_color(self):
    #     return self._color
    #
    # def set_color(self, color):
    #     print("Changing color to: ", color)
    #     self._color = color

    def get_color(self):
        return self._attributes['color']

    def set_color(self, color):
        print("Changing color to: ", color)
        self._attributes.get('color', None)

def main():
    donald = Duck(color = 'blue')
    print(donald.get_color())
    # steve = Duck(color = 'red')
    # print(steve.get_color())

if __name__ == "__main__": main()
