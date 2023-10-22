#!/usr/bin/python3
# containers.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print('This is the containers.py file.')

    t = tuple(range(25))
    print(t)
    print(type(t))
    print(10 in t)
    print(50 in t)
    print (50 not in t)
    print(t[10])

    x = list(range(25))
    print(x)
    x[10] = 25
    print(x)
    print(x.count(5))
    print(x.index(5))

    # List is mutable. Tuple is IMMUTABLE
    x.extend(range(20))
    print(x)
    x.insert(0, 25)
    print(x)
    # Remove a single element with value 25
    x.remove(25)
    # Delete element at index Y with "del"
    del x[25]

    print(x)

if __name__ == "__main__": main()
