#!/usr/bin/python3
# for.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():

    # For loop can use any iterator.
    # be it file input, containers, strings
    fh = open('lines.txt')
    for line in fh.readlines():
        print(line, end = "")

    for each_number in (1,2,3,4,5):
        print(each_number)

    for each_number in [1,2,3,4,5]:
        print(each_number)

    for each_character in 'string':
        print(each_character)


    # How about index?
    for i, a_char in enumerate('this is a string'):
        if a_char == 's':
            print("Index {} is an s ".format(i))


if __name__ == "__main__": main()
