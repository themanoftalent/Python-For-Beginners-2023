# *args  allows us to pass variable number of arguments to the function.
# Let’s take an example to make this clear.


def sum(*args):
    s = 0
    for i in args:
        s += i
    print ("sum is", s)


#pasing multiple args
sum(1)
sum(2,3)
sum(4,6)
sum(1)
sum(2,3,4,5,6)
sum(4,6,7,8,9,11)
sum(-19,4,6,7,8,9,11*8)