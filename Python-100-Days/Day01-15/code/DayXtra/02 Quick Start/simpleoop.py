class fibon:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def series(self):
        while True:
            yield (self.b)
            self.a, self.b = self.b, self.a + self.b


f = fibon(0, 1)
for r in f.series():
    if r > 500:
        break
    print(r)

print('\nSecond Method')


def fibR(number):
    if number == 1 or number == 2:
        return 1
    return fibR(number - 1) + fibR(number - 2)


print(fibR(7))
