def simpleGeneratorFun(n):

    while n<20:
        yield (n)
        n=n+1
    # return [1,2,3]

x = simpleGeneratorFun(1)
while True:
    try:
        val = next(x) # x.__next__() is "private", see @Aran-Frey comment
        print(val)
        if val == 10:
            break
    except StopIteration as e:
        print(e)
        break
