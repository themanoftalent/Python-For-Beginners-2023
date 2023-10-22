#!/usr/bin/python3
# exceptions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC
# No need to write extras notes here as you will have an extra licence file.

try:
    # we could say
    with open ('xLines.txt', 'r+') as fh:
        # to create teh file we maek the mode a # fh = open('xlines.txt')
        # #open any tex, the mode is not defined so the default mode is "r"
        for line in fh.readlines ():
            print (line)

except IOError as e:
    print ("Something bad happened! {}".format (e))

print ("After badness..")
