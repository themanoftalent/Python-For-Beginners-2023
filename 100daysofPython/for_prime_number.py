#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#
from math import sqrt

number = int(input('Enter a number: '))
finish = int(sqrt(number))
is_prime = True

for i in range(2, finish + 1):
    if number % i == 0:
        is_prime = False
        break
if is_prime and number != 1:
    print('%d is a prime number ' % number)
else:
    print('%d is not prime' % number)
