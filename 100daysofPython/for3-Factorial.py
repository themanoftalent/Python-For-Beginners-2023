#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

n = int(input('n = '))
result = 1
for x in range(1, n + 1):
    result *= x
print('%d! = %d' % (n, result))
