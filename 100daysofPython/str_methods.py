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

# Filename: str_method.py
# Description: basic function of str

name = "deercoder"

if name.startswith('de'):
    print 'string is startwith de'
if 'a' in name:
    print 'a is in the string'
if name.find('code') != -1:
    print 'found \'code\' in the string'

delimiter = "_*_"
mylist =['Brazil', 'Russia', 'India', 'China']
print delimiter.join(mylist)
