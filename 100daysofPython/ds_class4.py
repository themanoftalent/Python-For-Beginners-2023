#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

class maaslar:

    def __init__(self, maas1, maas2, maas3, maas4):
        self.dede = maas1
        self.emine = maas2
        self.derya = maas3
        self.akif = maas4
        self.toplam = maas1 + maas2 + maas3 + maas4


def printAll(self):
    print (self.dede)
    print(self.emine)
    print(self.akif)
    print(self.derya)
    print(self.toplam)
    #return (self.dede, self.emine, self.derya, self.akif, self.toplam)


def gider(self, gider1):
    self.gider1 = gider1


birinci = maaslar ('Dede : 2500', 'emine: 1750', ' derya :3300', ' akif : 3500')



printAll (birinci)
print ('*' * 32)
print ('Toplam maas geliri esittir %s' % (birinci.toplam))
# print ('Toplam maas geliri esittir %s' % (birinci.derya))
# print ('Toplam maas geliri esittir %s' % (birinci.akif))
# print ('Toplam maas geliri esittir %s' % (birinci.emine))


