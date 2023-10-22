#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

import math


def myGcd(num1, num2):
    if num1 == 0:
        print('It is 0 {num1} and {num2} equals {zero}'.format(a, b))

    while num2 != 0:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1


a = float(input('Enter the first number :'))
b = float(input('Enter the second number :'))

allgcd = myGcd(a, b)
print('{0} and {1} gcd is = {2}'.format(a, b, allgcd))

