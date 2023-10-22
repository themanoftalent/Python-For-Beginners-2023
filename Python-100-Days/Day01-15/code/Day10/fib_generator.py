#edited for python 3 and some basic arrangments
#!editor :Barish


def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

x = fib(100)

# Iterating over the generator object using next
print(x.__next__()); # In Python 3, __next__()
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())

# Iterating over the generator object using for in loop.
print("\nUsing for in loop")
for i in fib(100):
    print(i),
