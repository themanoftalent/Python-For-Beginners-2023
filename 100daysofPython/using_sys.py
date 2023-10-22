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

# Filename: using_sys.py
# Description: using sys modules.

import sys

print 'The commander arguments are:'
print 'The script path is', sys.argv[0]
for i in sys.argv:
    print i

print '\n\nThe PYTHONPATH is', sys.path, '\n'
