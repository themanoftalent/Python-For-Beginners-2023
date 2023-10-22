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

 a=input("enter a number=")
    try:
     if(int(a)>0):
        print(a+" is positive")
     elif(int(a)<0):
        print(a+" is negative")
     else:
        print("the given number is "+a)
    except:
        print("invalid entry")
