#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

def fiboon(n):
    a = 1
    b = 1

    for i in range (n - 1):
        a, b = b, b + a
    return a


print (fiboon (7))
