# for x in range (1, 11):
#     print (repr (x).rjust (2), repr (x * x).rjust (3), end=' ')
#     # Note use of 'end' on previous line
#     print (repr (x * x * x).rjust (4))


for sayi in range(1,21):
    print(repr(sayi).rjust(2),repr(sayi*sayi).rjust(3),end=' ')

    print(repr(sayi*sayi*sayi),repr(sayi*sayi*sayi*sayi).rjust(4))

    #  print(repr(sayi).rjust(2),repr(sayi*sayi).rjust(3),repr(sayi*sayi*sayi),repr(sayi*sayi*sayi*sayi).rjust(4))