a = [66.25, 333, 333, 1, 1234.5, 1]
print('The type is ',type(a))
print('Printing the list ',a)
print('Printing second element of the list  ',a[1])
print('Printing fourth element of the list  ',a[5])
a[0] = 2
print('Printing first element of the list  ',a[0])
print('-------------------------------')

s = 'hello'
print(s[2:4])
b = [87]
a[len(a):] = b
print('Printing the changed list ',a)

a.insert(0, 2)
a.insert(18, 2)
a.insert(-1, 2)
print(a.remove(1))
print(a.pop(0))

print(a.index(333))

print(a.count(333))
print(a.reverse())
print(a)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
[[apple[i] for apple in matrix] for i in range(4)]
# [i for i in range(4)]
# [apple[0] for apple in matrix]
