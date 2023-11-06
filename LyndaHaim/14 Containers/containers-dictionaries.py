#!/usr/bin/python3
# containers.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print('This is the containers.py file.')

    d1 = {'one' : 1, 'two' : 2, 'three' : 3}
    print(d1)

    d2 = dict(one = 1, two = 2, three = 3)
    print(d2)
    print(type(d1))
    print(type(d2))

    d3 = dict(four = 4, five = 5, **d2)
    print(d3)

    print('four' in d3)

    # Iterate over keys
    for k in d3: print(k)

    # or
    # Iterate over key/values
    for k, v in d3.items(): print(k, v)

    # dereference an entry in a dictionary by either
    print(d3['one'])
    # If the key doesn't exist, it will throw an error.
    # safer to do :
    print(d3.get('tenthousand')) # Default value specified in 2nd argument



if __name__ == "__main__": main()
