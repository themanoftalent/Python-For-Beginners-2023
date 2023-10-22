'''Lets create a class'''


class isimler:

    def sayitopla(self, sayi1):
        sayi1 = 10
        sonuc = sayi1 + 20
        print(sonuc)

    def baska_bir_fonk(self, bir_sisim):
        print("Buraya farkli bir fonk tanimlayabiliriz", bir_sisim, 'gibi')
        print("Buraya farkli bir isim %s gibi tanimlayabiliriz" % bir_sisim)  # doing it with format


ad = isimler()

ad.sayitopla(10)
ad.baska_bir_fonk('Ahmet')
