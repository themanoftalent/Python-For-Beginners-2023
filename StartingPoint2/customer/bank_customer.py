class Customer (object):
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError ('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        # print('{} {}'.format(self.balance))
        return self.balance


emir = Customer ('Emir kologlu', 300.0)
print(emir.deposit (546))
print(emir.withdraw (136))

print('--'*23)
jeff = Customer ('Jeff Knupp', 1000.0)
print(jeff.deposit (456))
print (jeff.withdraw (12))
