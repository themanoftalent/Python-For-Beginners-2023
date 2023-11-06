#!/usr/bin/python3
# containers.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print('This is the containers.py file.')

    t = 1,2,3,4,5
    print(t)
    print(t[0])
    print(t[4])
    print(t[-1])
    print(len(t))
    print(min(t))
    print(max(t))

    # Tuple created with commas, not necessarily parenthesis
    print((1))  # Just an integer
    print((1,)) # A 1-element tuple

    # Lists created with brackets
    list = [1,2,3,4,5]
    print(list)

if __name__ == "__main__": main()
