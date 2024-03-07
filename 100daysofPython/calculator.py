class Calculator:
    
    def __init__(self):
        self.result = 0
        self.history = []
        self.history.append(self.result)
        
    def reset(self):
        self.result = 0
        self.history = []
        self.history.append(self.result)
        
    def get_result(self):
        return self.result
    
    def get_history(self):
        return self.history
    
    def add(self, a):
        self.result += a
        self.history.append(self.result)
        return self.result
    
    def subtract(self, a):
        self.result -= a
        self.history.append(self.result)
        return self.result
    
    def multiply(self, a):
        self.result *= a
        self.history.append(self.result)
        return self.result
    
    def divide(self, a):
        if a != 0:
            self.result /= a
            self.history.append(self.result)
            return self.result
        else:
            raise ValueError("Cannot divide by zero")
        
    def undo(self):
        self.history.pop()
        self.result = self.history[-1]
        return self.result
    
    def redo(self):
        self.result = self.history[-1]
        return self.result
    
    def __str__(self):
        return str(self.result)

class AdvancedCalculator(Calculator):
    
    def __init__(self):
        super().__init__()
        self.history = []
        self.history.append(self.result)
        
    def power(self, a):
        self.result **= a
        self.history.append(self.result)
        return self.result
    
    def square_root(self):
        self.result **= 0.5
        self.history.append(self.result)
        return self.result
    
    def __str__(self):
        return str(self.result)
    
# now make the code work
calculator = AdvancedCalculator()
print(calculator.get_result())
print(calculator.add(2))
print(calculator.subtract(1))
print(calculator.multiply(3))
print(calculator.divide(2))
print(calculator.power(2))
print(calculator.square_root())
print(calculator.undo())
print(calculator.redo())
print(calculator.get_history())
print(calculator.reset())




