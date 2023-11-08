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


start=int(input("enter the starting:"))
end=int(input("enter the ending"))
if(start>end):
    print("invalid range")
try:
    if((end-start)==1):
        print("Range is too small")
    for i in range (start+1,end):
        sum=0
        count=0
        a=i
        while (a>0):
            dig=a%10
            sum+=dig**3
            a//=10
        if i==sum:
            print(i)
except:
    print("Invalid input")
