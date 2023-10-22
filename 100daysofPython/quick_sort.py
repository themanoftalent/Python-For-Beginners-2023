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

def quickSort(A):
    if len(A) < 2:
        return A
    pivot = A[0]
    B = [i for i in A if i < pivot]
    C = [i for i in A if i > pivot]
    return quickSort(B) + [pivot] + quickSort(C)

print (quickSort([2,1,4,3,6,5]))
print (quickSort([7,6,5,4,3,2,1]))
