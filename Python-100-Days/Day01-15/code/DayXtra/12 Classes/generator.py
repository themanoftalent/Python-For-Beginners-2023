#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class inclusive_range:
    def __init__(self, *args):
        numargs = len(args)
        if numargs < 0:
            raise TypeError("Requires at least 1 argument")
        elif numargs == 1:
            self.start = 0
            self.stop = args[0]
            self.step = 1
        elif numargs == 2:
            (self.start, self.stop) = args
            self.step = 1
        elif numargs == 3:
            (self.start, self.stop, self.step) = args
        else:
            raise TypeError("Expected at most 3 arguments. got {}".format(numargs))

    def __iter__(self):
        i = self.start
        while i <= self.stop:
            yield i
            i+= self.step


def main():
    o = inclusive_range(25)
    #o = inclusive_range(5, 25)
    #o = inclusive_range(5, 25, 2)
    #Error: too many arguments
    ## o = inclusive_range(5, 25, 2, 25)
    #Error No args
    #o = inclusive_range()

    for i in o: print(i, end = ' ')

if __name__ == "__main__": main()
