def fib(n):
    if n==0 or n==1:
        return n
    else:
        a, b = 0, 1
        for i in range(2,n):
            a, b = b, a + b
            # print a, b
        return a+b

print (fib(800))
