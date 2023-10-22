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

try:
    num = int(input("Enter a number: "))
    if(num>1000):
        print("enter less than 1000")
    elif num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print("no")
                break
        else:
            print("yes")
    else:
        print("no")
except:
    print("Invalid Entry")
