'''bir sinif yaratalim ve bu seinfta
bazi islemler yapalim
fonk tanimlayalim'''


class azami:
    lamba = ['python', 'cython'] #liste tanimlandi
    sozluk = {1: 'lisp', 2: 'php'} #burada ise sozluk tanimlandi

    def __init__(self): #baslatici, yani initilizator
        if 1 in self.sozluk:
            print(self.sozluk)

    def yaziyor(self):
        if 'python' in self.lamba:
            print(self.lamba)


bul = azami()
bul.yaziyor()
