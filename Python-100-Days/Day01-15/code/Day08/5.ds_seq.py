shoplist = ['apple', 'mango', 'carrot', 'banana'] #multi array
name = 'Alisa'

# Indexing or 'Subscription' operation #
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character\n')
print('Character 0 is', name[0])
print('Character 1 is', name[1])
print('Character 2 is', name[2])
print('Character 3 is', name[-3])
print('Character\n')

# Slicing on a list #
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])
print('\nSlicing')
# Slicing on a string #
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])
print('\n')
print(shoplist)
print('\n')
del shoplist[0]
print('after deleting first item')
print(shoplist)