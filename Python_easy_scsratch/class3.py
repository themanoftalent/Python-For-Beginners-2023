#Inheritence
'''\
class parent():
    def fonksiyon1(self):
        print("This is the parent class")


class child(parent):
    def __init__(self):
        print("This is the child class")


c = child()
#c.f2()
c.fonksiyon1()
'''
# Multiple Inheritence

class makina_ogrenme():
    def fonksiyon1(self):
        print("This is machine learning ")

class web_development():
    def __init__(self):
        print("Flask and Django are Python web frameworks")


class yapay_zeka():
    def fonksiyon2(self):
        print("Sadece yapay zeka yaziyor. This is Artificial Intelligence ")


class python(makina_ogrenme, web_development,yapay_zeka):
    pass


class sadeceYz(yapay_zeka):
    pass


yazar=sadeceYz()
yazar.fonksiyon2() #ayri taimladik


yaz = python()
yaz.fonksiyon1()
#yaz.fonksiyon2() #beraber tanimladik
