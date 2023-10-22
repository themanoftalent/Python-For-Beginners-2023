#! /usr/bin/python

#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

number = 23
running = True

while running:
	guess = int(raw_input("please input a number:"))
	if guess == number:
		print('OK')
		running = False
	elif guess > number:
		print('Big')
	else:
		print('Small')

print('loop over')
