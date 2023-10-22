'''repr() fonksiyonu ise ASCII olmayan karakterlerle karşılaşsa bile, 
bize çıktı olarak bunların da karakter karşılıklarını gösterir:'''


class Man:
    name='Heman'

    def __repr__(self):
        return 'Hello '+ self.name



adam1=Man()

print(repr(Man()))

print(adam1.name)