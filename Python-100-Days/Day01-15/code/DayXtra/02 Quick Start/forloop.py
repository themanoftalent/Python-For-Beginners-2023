#!/usr/bin/python3
# for and range
_author_ = 'archer'

# read the lines from the file
fh = open ('lines.txt')
for line in fh.readlines ():
    # Print statement 'end' argument in Python 3 allows overriding the end-of-line character which
    # defaults to '\n'. Each line in the file already has a carriage return so the end-of-line is not needed.
    print (line, end="")
