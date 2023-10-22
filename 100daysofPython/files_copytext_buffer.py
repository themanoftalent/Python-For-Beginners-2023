#!/usr/bin/python3
# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    infile = open('bigfile.txt', 'r')
    outfile = open('bigfile_copy.txt', 'w')
    buffersize = 50000 # bytes
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        buffer = infile.read(buffersize)


if __name__ == "__main__": main()
