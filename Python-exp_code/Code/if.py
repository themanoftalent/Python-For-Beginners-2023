#! /usr/bin/python
number = 23
guess = int(raw_input("please input a number:"))

if guess == number:
	print("OK")
elif guess < number:
	print("Small")
else:
	print("Big")

print("done") 

