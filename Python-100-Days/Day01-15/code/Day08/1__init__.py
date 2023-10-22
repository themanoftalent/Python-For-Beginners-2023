# init is initializing
"""self as it suggests, refers to itself- the object which has called the method.
That is, if you have N objects calling the method, then self.a will refer to a separate
instance of the variable for each of the N objects. Imagine N copies of the variable a for each object
__init__ is what is called as a constructor in other OOP languages such as C++/Java. The basic idea is
 that it is a special method which is automatically called when an object of that Class is created
"""


class Person:
    """Document - Inside Class """

    def __init__(self, name):
        """Document - __init__ Constructor"""
        self.n_name = name

    def show(self, n1, n2):
        """Document - Inside Show"""
        print(self.n_name)
        print('Sum of the numbers  = ',(n1 + n2))

    def __del__(self):
        print('Destructor Deleting object - ', self.n_name)


p = Person('Jay Kay')
p.show(2, 3)
print(p.__doc__)
print(p.__init__.__doc__)
print(p.show.__doc__)

print('\n')
p2=Person('Nazan Kaya')
p2.show(45,43)
