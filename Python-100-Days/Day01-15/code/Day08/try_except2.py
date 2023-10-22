try:
    bolunen = int(input("bölünecek sayı: "))
    bolen = int(input("bolen sayı: "))
except ValueError:
    print("Lütfen sadece sayı girin!")
else:
    try:
        print(bolunen/bolen)
    except ZeroDivisionError:
        print('You cannot divide a number to zero')
