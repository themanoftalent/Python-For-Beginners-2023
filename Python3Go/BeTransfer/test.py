class Calculator: 
    def __init__(self):
        self.curValue = 0
    def __repr__(self):
        return "my Calculator"
    def subtract(self, number):
        self.curValue -= number
    def add(self, number):
        self.curValue += number

mycalc = Calculator()
mycalc.add(12)
mycalc.subtract(10)
print mycalc.curValue
print mycalc

