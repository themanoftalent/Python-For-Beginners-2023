#!/usr/bin/python3
# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    infile = open('lines.txt', 'r')
    outfile = open('output.txt', 'w')
    for line in infile:
        print(line, file = outfile, end = '')

if __name__ == "__main__": main()
