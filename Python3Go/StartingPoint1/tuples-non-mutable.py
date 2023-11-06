my_tuple = (4, 2, 3, [6, 5]) #3 un 0=6 sonra 9 olacak

# we cannot change an element
# If you uncomment line 8
# you will get an error:
# TypeError: 'tuple' object does not support item assignment

#my_tuple[1] = 9 normal tuple degismez

# but item of mutable element can be changed
# Output: (4, 2, 3, [9, 5])
my_tuple[3][0] = 9
print(my_tuple)


# my_tuple[4].append = 7
# print(my_tuple)

# tuples can be reassigned
# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
my_tuple = ('p','r','o','g','r','a','m','i','z')
print(my_tuple)