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
import re

text = 'abbaaabbbbaaaaa'
pattern = 'ab'

for mstch in re.finditer(pattern, text, flags=re.IGNORECASE):
    s = mstch.start()
    e = mstch.end()

print('Matching found "%s" at %d:%d' % (text[s:e], s, e))
