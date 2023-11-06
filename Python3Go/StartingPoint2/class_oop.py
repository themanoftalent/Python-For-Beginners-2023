class Animalsactions:
    def qwack(self): return self.strings['qwack']
    def fur(self):   return self.strings['fur']
    def bark(self):  return self.strings['bark']
    def meov(self):  return self.strings['meov']

class Ordek(Animalsactions):
    strings = dict(
        qwack='Duck qwaks',
        fur='Duck has fur',
        bark='Duck no bark',
        meov='Duck no meov'
    )

class Insan(Animalsactions):
    strings = dict(
        qwack='Insan can dwakcs',
        fur='Insan has fur',
        bark='Insan can bark',
        meov='Insan can meov'
    )

class Kopek(Animalsactions):
    strings = dict(
        qwack='Dog cannot dwakcs',
        fur='Dog has fur',
        bark='Dog can bark',
        meov='Dog cannot meov'
    )


def yazdirKopek(kopek):
    print(kopek.bark())
    print(kopek.fur())
    print(kopek.meov())
    print(kopek.qwack())
def yazdirOrdek(ordek):
    print(ordek.qwack())
    print(ordek.meov())
    print(ordek.fur())
    print(ordek.bark())
def yazirInsan(insan):
    print(insan.meov())
    print(insan.fur())
    print(insan.qwack())
    print(insan.bark())



def main():
    Donald = Ordek()
    Tumaz = Kopek()
    Ahmet = Insan()

    print('*****yazdir kopek****')
    for o in (Donald, Ahmet, Tumaz):
        yazdirKopek(o)


if __name__ == '__main__': main()
