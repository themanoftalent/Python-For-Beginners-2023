odds=set([1,3,5,7,9])
#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

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