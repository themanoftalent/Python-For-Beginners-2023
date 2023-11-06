#!/usr/bin/python3
# to find if the number is prme or not
def isprime(number):
    if number == 1:
        print ("1 is special")
        return False


    for i in range (2, number):
        if number % i == 0:
            print ("{} equals {} x {}".format (number, i, number // i))
            return False

        #it works fine without else,but ident is problem
        else:
            print (number, "is a prime number")
        return True


for number in range (1, 20):
    isprime (number)
