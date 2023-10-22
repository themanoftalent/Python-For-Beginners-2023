try:
    bolunen = int(input('Enter a number'))
    bolen = int(input('Enter another number  '))
    result = bolunen / bolen
    print('bolunen/bolen')
except ValueError:
    print('Enter a number')


except ZeroDivisionError:
    print("0 ile bolunme sorunu, hata divided by zero!, 404 anan")
