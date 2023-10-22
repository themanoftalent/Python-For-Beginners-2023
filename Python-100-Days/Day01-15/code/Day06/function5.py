def formula1(a, b=5, c=10):
    return (a + b) * 2 + (c * 3)



print(formula1(1, 2, 3))
print(formula1(100, 200))
print(formula1(100))
print(formula1(c=2, b=3, a=1))


def f2(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


f2(1,2,3,4,5,6,7,8,9,10)