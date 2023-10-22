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

x="HELLO"
n=input("Enter number of times that HELLO is needed to be printed:")
try:
    i=0
    while(i<int(n)):
        print (x)
        i+=1
except:
    print("invalid entry")
