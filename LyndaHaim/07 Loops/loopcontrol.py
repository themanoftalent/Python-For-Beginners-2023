#!/usr/bin/python3
# 2.break.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    s = 'this is a string'

    # Print string and skip all s's.
    for c in s:
        if c == 's':
            continue
        print(c, end='')

    print()
    # Print string and stop at first s.
    for c in s:
        if c == 's':
            break
        print(c, end='')

    print()

    # For Loop Else continues after last iterator value.
    for c in s:
        print(c, end='')
    else:
        print("else")


if __name__ == "__main__": main()
