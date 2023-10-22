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

# Filename: using_module.py
# Description: using module and __name__

if __name__ == '__main__':
    print 'This is main'
else:
    print 'This is sub module'

## If using it directly by 'python using_module.py' or 
## './using_module.py', then it is excuted by main
## otherwise if it is used by import using_module, then
## it is excute by sub module.
