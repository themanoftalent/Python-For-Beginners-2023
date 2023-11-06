def remove_dupl(values):
    output = []
    seen = set ()
    for value in values:
        if value not in seen:
            output.append (value)
            seen.add (value)
    return output


values = ['Akif', 'Akif', 'Derya', 'Derya', 'Leyla', 'Zeynep', 'Hulya', 'Ayse']
result = remove_dupl (values)
list = set (result)

print (result)
print (sorted (result))
print ('secod_method' + ' ' * 28 + 'second method')

valum = (1, 1, 1, 12, 2, 3, 4, 5, 6, 6, 6, 5, 4, 3, 6, 7, 8, 8, 9, 9,
         4, 9, 9, 11, 1, 1, 11, 14, 14, 15, 15)
set = set (valum)
print ('{:>3}'.format (' '), end=' ')
print (set)
# the list is auto sorted


