class Square:

    def __init__(self):  # special method __init__
        self.sides = 4

    def carp(self, yan, uzun):
        toplam = yan * uzun ** 2
        return toplam

    def kenar(self, kenarB=34, hanarK=120):
        print(kenarB + hanarK)


square = Square()
print(square.sides)
print(square.carp(5, 3))
square.kenar()


class Car:
    def __init__(self, color):
        self.color = color

    def marka(self, amblem):
        self.amblem = amblem
        return amblem


car = Car("blue")  # Note: you should not pass self parameter explicitly, only color parameter

print(car.color)
print(car.marka('audi'))
