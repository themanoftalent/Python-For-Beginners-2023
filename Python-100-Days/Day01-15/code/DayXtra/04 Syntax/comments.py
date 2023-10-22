#!/usr/bin/python3
# comments.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    for n in primes():
        if n > 100: break
        print(n)

def isprime(n): # Generate a list of prime numbers
    if n == 1:
        return False        # One is never prime
    for x in range(2, n):
        if n % x == 0:
            return False    # Found a divisor
    else:
        return True

def primes(n = 1):
   while(True):
       if isprime(n): yield n   # Yield makes this a generator
       n += 1 

if __name__ == "__main__": main()
