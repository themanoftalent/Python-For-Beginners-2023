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

f: #test1.txt ayri bir dosya olarak yanda
    reado = open ('test1.txt', 'r')
    size_to_read = 30
    f_contents = f.read (size_to_read)
    while len (f_contents) > 0:
        print (f_contents)
        f_contents = reado.read (size_to_read)
