import sys
a=2
print(type(a))

x,y,z=1,2,3
print("x is {} y is {} z is {}".format(x,y,z))

p,q=1,2
print("Before swap : p is {} q is {}".format(p,q))
p,q=q,p
print("After swap : p is {} q is {}".format(p,q))

l,m,n=[1,2,3]
print("l is {} m is {} n is {}".format(l,m,n))

#assign tuple to multiple variables 
d,e,f=(1,2,3)
print("d is {} e is {} f is {}".format(d,e,f))
''' None is 
    absence of value
    *******'''
abc=None
print(type(abc))
