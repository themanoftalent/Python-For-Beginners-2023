#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
# 


import math


try:
	number=int(input('Enter a number'))
except IOError:
	print('Wrong input')
	if number<0:
		print('Negative number')
except ZeroDivisionError:
	print('Try again zero division')
finally:
	print('The square of {} is {:}'.format(number, math.sqrt(number)))
