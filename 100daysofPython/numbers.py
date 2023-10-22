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
#  !/usr/bin/python
#  Copyright (c) akifciftci 2019. Aim to help new beginner to try hard and learn more.
#
import math  # This will import math module

anumber = 5

print(anumber)
print()
print(type(anumber))

print(type(5.0))

c = 5 + 3j
print(c + 3)

print((isinstance(c, complex)))

print('==========================')
print(int(2.3))
print(float(5))
print((complex('3+5j')))

print('=========================')
# now
# Number        System	      Prefix
# Binary	     '0b'    or    '0B'
# Octal	         '0o'    or    '0O'
# Hexadecimal	 '0x'    or    '0X'


print((0b1101011))

print((0xFB + 0b10))

print((0o15))

# ===============================

print('')
print("abs(-45) : ", abs(-45))
print("abs(100.12) : ", abs(100.12))
print("abs(119) : ", abs(119))
print('=========================')



print("math.ceil(-45.17) : ", math.ceil(-45.17))
print("math.ceil(100.12) : ", math.ceil(100.12))
print("math.ceil(100.72) : ", math.ceil(100.72))
print("math.ceil(119L) : ", math.ceil(119))
print("math.ceil(math.pi) : ", math.ceil(math.pi))


print('=========================')

num = int(input('Enter a number : '))
# To take input from the user
# num = int(input("Display multiplication table of? "))
# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)
