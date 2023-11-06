#!/usr/bin/python3
# conditionals.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print("This is the conditionals.py file.")

    a, b = 0, 1
    if a < b:
        print("'a' is less than 'b'")
    else:
        print("'a' is NOT less than 'b'")

    # You can also write this in a  single line
    v = "'a' is less than 'b'" if a < b else "'a' is not less than 'b'"
    print(v)

    # elif statement
    v = 'two'
    if v == 'one':
        print("V is one")
    elif v == 'two':
        print("V is two")
    elif v == 'three':
        print("V is three")
    else:
        print("v is some other thing")


if __name__ == "__main__": main()
