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

# Filename: tuple.py
# Description: a simple for tuple

zoo = ('wolf', 'elephant', 'penguin')
print 'Number of ainals is', len(zoo)

new_zoo = ('monkey', 'snake', 'rabbit', zoo)
print 'Number of new_zoo is', len(new_zoo)
i = 0
while i < len(new_zoo):
    print new_zoo[i],
    i = i + 1 
print '\nEnding output'
