##################################################
#### **************************************** ####
#### !/usr/bin/python3                        ####
#### -*- coding: utf-8 -*-                    ####
#### @Time    : 2023/20/10 11:40              ####
#### @Author  : themanoftalent                ####
#### @Site:https://github.com/themanoftalent  ####
#### @Project : python-app                    ####
#### **************************************** ####
##################################################learn more.
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
