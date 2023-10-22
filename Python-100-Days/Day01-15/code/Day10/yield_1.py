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
        if val == 20:
            break
    except StopIteration as e:
        print(e)
        break



# At each iteration you're advancing the iterator 3 times by making
#  calls to x.__next(). There are usually better patterns in python
# where you don't need to make calls to next directly. For example,
# if you have finite iterator, use a for loop to automatically breaks
#  on StopIteration:
#
# x = simpleGeneratorFun(1)
# for i in x:
#     print i
