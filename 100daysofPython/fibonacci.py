
#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

a = 0
b = 1
for _ in range(100):
    a, b = b, a + b
    print(a, end=' ')
