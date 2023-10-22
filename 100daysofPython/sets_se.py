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

# evens=(2,4,6,8,10) tuple
evens={2,4,6,8,10}
primes={2,3,5,7}
composites=set([4,6,8,9,10])

# print(type(odds))
# print(type(evens))

print(odds.union(evens))
print(odds.union(composites))
print(evens.union(composites))
print(evens.union(odds))
print('==================================')


print(odds.intersection(evens))
print(odds.intersection(composites))
print(evens.intersection(composites))
print(composites.intersection(odds))
