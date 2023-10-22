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

#edited for python 3 and some basic arrangments
#!editor :Barish

def passFun():
    print ('abc')
    pass
    i=0
    while True:
        if i==1000: #break added
            break
        print ('loop', i)
        i += 1
        pass


passFun();
