#!/usr/bin/python3
# ops.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print("This is the ops.py file.")

    # Python by default prints decimal values
    print(5)
    print(0b0101)

    # Write a function to output in binary
    def b(n): print('{:08b}'.format(n))

    b(5)

    x, y = 0x55, 0xaa

    print("x = ", end = "")
    b(x)
    print("y = ", end = "")
    b(y)
    # Bitwise or
    print("x | y = ", end = "")
    b(x | y)
    # Bitwise and
    print("x & y = ", end = "")
    b(x & y)
    # Exclusive Or
    print("x ^ y = ", end = "")
    b(x ^ y)
    print("x ^ 0 = ", end = "")
    b(x ^ 0)
    print("x ^ 0xff = ", end = "")
    b(x ^ 0xff)
    print("x << 4 = ", end = "")
    b(x << 4)
    print("x >> 4 = ", end = "")
    b(x >> 4)

    # 1s complement operator
    print("~ x = ", end = "")
    b(~ x)

if __name__ == "__main__": main()
