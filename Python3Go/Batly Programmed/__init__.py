# init is initilaizing
'''self as it suggests, refers to itself- the object which has called the method.
That is, if you have N objects calling the method, then self.a will refer to a separate
instance of the variable for each of the N objects. Imagine N copies of the variable a for each object
__init__ is what is called as a constructor in other OOP languages such as C++/Java. The basic idea is
 that it is a special method which is automatically called when an object of that Class is created
'''

class Nurses:



    def __init__(self, firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName

    @property
    def display(self):
        return '{} {}'.format(self.firstName, self.lastName)


    @display.setter
    def display(self,name):
        firstName,lastName=name.split(' ')
        self.firstName = firstName
        self.lastName = lastName
        






n1=Nurses('Jane', 'Mcdonald')

n1.display='Jack Sparrow'

print(n1.display)
        