#get nth value in fibonacci sequence
class fib:
    def __init__(self):
        self.savedVals = {}
    def getNth(self,n):
        if n in [0,1]:
            return n
        if n in self.savedVals:
            return self.savedVals[n]
        else:
            result =self.getNth(n-1)+self.getNth(n-2)
            self.savedVals[n] = result
            return result
myfib = fib()
print myfib.getNth(90)
