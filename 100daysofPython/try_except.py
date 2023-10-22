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

import random
import os
import sys

try:
    aNum = int (input ('Enter a number :'))

except ValueError:

    if aNum > 0 and aNum < 100:
        print ('Correct', aNum)
    else:
        print ('Try again')
