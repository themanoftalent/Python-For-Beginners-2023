def fib(limit):
    a, b = 0, 1
    while a + b < limit:
        a, b = b, a + b
    return b

x = fib(100)
print (x)
