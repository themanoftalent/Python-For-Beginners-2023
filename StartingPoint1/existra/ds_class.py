class merhaba:

    def login(self, kadi):
        kadi = (int (input ('Enter a password')))
        while kadi != 123:
            break

    def selam(self, isim, yas, memleket):
        self.isim = isim
        self.yas = yas
        self.memleket = memleket
        print (isim, yas, memleket)


kadi = merhaba ()
while kadi==123:
    continue
kadi.login (kadi)

kadi.selam ('Ahmet', 24, 'istanbul')
