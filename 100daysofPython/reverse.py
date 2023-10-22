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

a = "Jabba Laci"
li = []
li.extend(a)
print li
size = len(li)
for i in range(0,size/2):
    li[i], li[size-1-i] = li[size -1-i], li[i]
print li

