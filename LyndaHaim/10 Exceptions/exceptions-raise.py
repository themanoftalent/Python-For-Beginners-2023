#!/usr/bin/python3
# exceptions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

def main():
    try:
        for line in readfile('xlines.doc'): print(line.strip())
    except IOError as e:
        print("Cannot read file: ", e)
    except ValueError as v:
        print("Bad FileName: ", v)

def readfile(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else:
        raise ValueError('FileName must end with .txt')

if __name__ == "__main__": main()
