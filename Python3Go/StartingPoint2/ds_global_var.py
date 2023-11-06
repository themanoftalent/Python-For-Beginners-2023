# # Declare a variable and initialize it
# f = 101
# print (f)
#
#
# # Global vs. local variables in functions
# def someFunction():
#     global f
#     f = 'I am learning Python'
#     # print (f)
#
#
# someFunction ()
# print (f)

print ('==' * 14)

fa = 102
print (fa)


# Global vs.local variables in functions
def somedFunction():
    global fa


print (fa)
fa = "changing global variable"

somedFunction ()
print (fa)
