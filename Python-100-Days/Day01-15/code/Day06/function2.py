#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#


# if a number rater than the other they change place
def gcd(x, y):
    if x > y:
        (x, y) = (y, x)

    return x, y


print(gcd(63, 56))
