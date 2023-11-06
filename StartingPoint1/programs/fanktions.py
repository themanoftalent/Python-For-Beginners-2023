def my_func():
    a_number = 10
    print ("Value inside function:", a_number)


# a new function
a_number = 20  # value outside of the function
my_func ()
print ("Value outside function:", a_number)


def lolFunc(x, y):
    nomo = x ** y
    print ('3 power of 2 is ', nomo)
    return nomo


lolFunc (2, 3)


# function three

def take_fack(n):

    if n == 1:
        print ('It is just one')
    else:
        print(n*take_fack(n-1))

number=4
take_fack(2)
