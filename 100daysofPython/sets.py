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
#

letsets={'hello'}
print(type(letsets))
letsets.add('This is ')

print(dir(letsets))

letsets.add('No where is ')
letsets.add(None)
letsets.add(123214)

print(letsets.pop())

print(letsets.pop())
print(letsets)
