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

from random import randint

face = randint(1, 6)
if face == 1:
    result = 'BIR'
elif face == 2:
    result = 'IKI'
elif face == 3:
    result = 'UC'
elif face == 4:
    result = 'DORT'
elif face == 5:
    result = 'BES'
else:
    result = 'ALTI'
print(result)
