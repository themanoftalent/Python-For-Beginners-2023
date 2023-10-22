#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

# vowels list
vowels = ['a', 'e', 'i', 'o','e','e', 'i', 'u','a', 'a', 'a', 'a']

# count element 'i'
count = vowels.count('a')

# print count
print('The count of i is:', count)

# count element 'p'
count = vowels.count('p')

# print count
print('The count of p is:', count)
print('============RASTGELE===============')

# random list
rastgele = ['a', ('a', 'b'), ('a', 'b'), [1, 4],('a', 'b')]

# count element ('a', 'b')
count = rastgele.count(('a', 'b'))
# print count
print("The count of ('a', 'b') is:", count)

# count element [3, 4]
count = rastgele.count([1, 4])

# print count
print("The count of [1, 4] is:", count)