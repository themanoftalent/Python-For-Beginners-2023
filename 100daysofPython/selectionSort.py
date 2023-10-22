##################################################
#### **************************************** ####
#### !/usr/bin/python3                        ####
#### -*- coding: utf-8 -*-                    ####
#### @Time    : 2023/20/10 11:40              ####
#### @Author  : themanoftalent                ####
#### @Site:https://github.com/themanoftalent  ####
#### @Project : python-app                    ####
#### **************************************** ####
##################################################

numbers = [26,1,54,93,17,77,31,44,55,20]
for i in range(len(numbers)-1,0,-1):
	max = 0
	for k in range(i):
		if numbers[k] > max:
			max = numbers[k]
			savedSpot = k
	numbers[savedSpot] = numbers[i]
	numbers[i] = max
print numbers
	
