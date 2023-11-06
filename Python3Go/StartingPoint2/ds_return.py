def kare(x):
    return x * x


print (kare (2))

print (kare (5))

print ('--' * 18)


def guru(*args):
    print (args)


guru (1, 2, 3, 4, 5, 6, 7, 8, 9)  # Multiple arguments can be passed as an array

print ('--' * 28)


# define a function
def func1():
    print ("I am learning Python function", end=' ')
    print ("still in func1")


func1 ()


def square(x):
    return x * x


print (square (4))


def multiply(x, y=0):
    print ("value of x=", x)
    print ("value of y=", y)

    return x * y


print (multiply (y=2, x=4))
