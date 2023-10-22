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

def simpleGeneratorFun(n):

    while n<20:
        yield (n)
        n=n+1
    # return [1,2,3]

#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

x = simpleGeneratorFun(1)
while True:
    try:
        val = next(x) # x.__next__() is "private", see @Aran-Frey comment
        print(val)
        if val == 10:
            break
    except StopIteration as e:
        print(e)
        break
