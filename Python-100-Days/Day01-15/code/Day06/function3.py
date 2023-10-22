def ApplyFilter(mystr):
    return len(mystr) == 6


print(hex(ord('A')))
print(abs(-1.234534))
print(round(-1.2345232))
print(pow(1.2345, 532))

print('====================')

fruit = ['Apple', 'Banana', 'Plum', 'Orange']
print(fruit[slice(1, 3)])

fruits2 = list(filter(ApplyFilter, fruit))


print(fruit)
print(fruits2)
