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

squares=[]
for i in range(1,101):
    print(i**2)

print('===='*30)

#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

#in other ways short

squares2=[i**2 for i in range(1,101)]
print(squares2)

#we can improve this such
print('===='*30)

squaresReminder=[i**2 %5 for i in range(1,101)]
print(squaresReminder)

print('===='*30)

squaresReminder=[i**2 //(113/17) for i in range(1,101)]
print(squaresReminder)

print('===='*30)
print(dir(squares2))
print(help(squares2.pop))
