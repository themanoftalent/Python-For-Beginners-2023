#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)


print(fibo(8))

# ========================================================================
# print ( fibo ( int(input("Enter a number to calculate fibonnaci "))) )

# ## Example 2: Using recursion
# def fibR(n):
#  if n==1 or n==2:
#   return 1
#  return fibR(n-1)+fibR(n-2)
# print (fibR(8))


# class fibon:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def series(self):
#         while True:
#             yield (self.b)
#             self.a, self.b = self.b, self.a + self.b
#
#
# f = fibon(0, 1)
#
# for r in f.series():
#     if r > 100:
#         break
#     print(r)
