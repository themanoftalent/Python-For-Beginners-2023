#!/usr/bin/python3
# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    a = 7
    print(type(a), a)
    print("This is the syntax.py file.")

    a, b = 0, 1
    a, b = 1, 1
    a, b = 2, 1

    if a < b:
        print("a is less than b")
    elif a > b:
        print("a is greater than b")
    else:
        print("a is equal to b")


    # Tertiary conditional form
    s = "Less than" if a < b else "Not less than"
    print(s)



if __name__ == "__main__": main()
