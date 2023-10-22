#!/usr/bin/python3
# exceptions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

def main():

    # Try to open a file that does not exist
    try:
        fh = open('file_does_not_exist.txt')
    except IOError as e:
        print("Could not open file: ",e)
    else:
        for line in fh: print(line.strip())

# You can raise exceptions with the 'raise' statement

if __name__ == "__main__": main()
