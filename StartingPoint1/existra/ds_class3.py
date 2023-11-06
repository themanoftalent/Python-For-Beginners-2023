class Employee:

    def __init__(self, first, second, payment, birth):
        self.first = first
        self.second = second
        self.payment = first
        self.birth = birth
        self.mail = first + second + '@' + 'company.com'


def printFullNameSurname(self):
    print ('{} {}'.format (self.first, self.second))  # print burada yapilmistir
    return ('{} {}'.format (self.first, self.second))


emp1 = Employee ('Emine', 'YILMAZ', 1700, 1958)
emp2 = Employee ('Mevlut', 'ALKAN', 2400, 1926)

print (emp1.__dict__)
print (emp2.__dict__)
# print(vars(emp2))  #tumunu bu sekilde ekrana yazdirabiliriz oteyandan teker teker de yazabiliriz.
# we can print in this mode as well

print ('\n' * 2)

printFullNameSurname (emp2)
# print(emp1.FullNameSurname())

print (printFullNameSurname (emp1))
# print(printFullNameSurname(emp2))


# #soylede yazabilirdik
# print('{} {}'.format(emp1.first, emp1.second)) #yalniz bunu bir mothoda ceviriesek daha iyi olur
# #such as we are creating a method which returns the values as

# anotherway is  name of the class

# print (Employee.printFullNameSurname (emp1))
