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

class Man:
    name='Heman'

    def __repr__(self):
        return 'Hello '+ self.name



adam1=Man()

print(repr(Man()))

print(adam1.name)
