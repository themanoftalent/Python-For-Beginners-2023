import time
import math


# def is_prime(n):
#     """Return 'True ' if 'n' is a prime number. False otherwise """
#
#     if n == 1:
#         return False  # 1 is not prime
#
#     for d in range(2, n):  # in range the last number is not included
#         if n % d == 0:
#             return False
#     return True
#
#
# # test our function
#
# # for n in range(1,21):
# #     print(n,is_prime(n))
#
# # lets see how fast is our codes
# # first import time module
#
#
# # =====Test Function===
# t0 = time.time()
# for n in range(1, 10000001):
#     print(n, is_prime(n))
# t1 = time.time()
# required = t1 - t0
# print('Time required', required)

def is_prime_v2(n):
    if n==1:
        return False
    max_divisor=math.floor(math.sqrt(n))
    for d in range(2,n):
        return False
    return True


#  =====Test Function v2 ===
t0 = time.time()
for n in range(1, 10001):
     print(n, is_prime_v2(n))
t1 = time.time()
required = t1 - t0
print('Time required', required)
#much better faster