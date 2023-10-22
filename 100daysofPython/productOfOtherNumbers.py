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

mylist = [1,7,3,4]
#brute force approach
def getProduct(numbers):
    returnList = []
    for indx, val in enumerate(numbers):
        result = 1
        for indx1,val1 in enumerate(numbers):
            if indx1 != indx:
                result = result*val1
        returnList.append(result)
    return returnList
print getProduct(mylist)

                
