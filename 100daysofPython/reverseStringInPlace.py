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

#reverse a string in place
def reverse(string):
    mylist = list(string)
    b = ""
    sizeL = len(mylist)
    for indx,val in enumerate(mylist):
        if indx >= sizeL/2:
            b = mylist[sizeL-1-indx]
            mylist[sizeL-1-indx] = mylist[indx]
            mylist[indx] =  b
        
    print mylist
reverse("hellow")
