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
with open("camelot.txt",'w') as f:
    for i in range(100):
        f.write("We're the knights of the round table We dance whenever we're able"+str(i))



with open("camelot.txt",'r') as f:
    for line in f:
        print(line)
        break


