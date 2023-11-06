# Best practice, as it were, is best practiced whence much practice has been done without consideration for it.

tup1 = ('Robert', 'Carlos', '1965', 'Terminator 1995', 'Actor', 'Florida');
tup2 = (1, 2, 3, 4, 5, 6, 7);
print (tup1[0])
print (tup2[1:4])

# Packing and Unpacking
x = ("Guru99", 20, "Education")  # tuple packing
(company, emp, profile) = x  # tuple unpacking
print (company)
print (emp)
print (profile)

# Comparing tuples
# case 1
a = (5, 6)
b = (1, 4)
if (a > b):
    print ("a is bigger")
else:
    print ("b is bigger")

# case 2
a = (5, 6)
b = (5, 4)
if (a > b):
    print ("a is bigger")
else:
    print ("b is bigger")

# case 3
a = (5, 6)
b = (6, 4)
if (a > b):
    print ("a is bigger")
else:
    print ("b is bigger")

# Tuples and dictionary
a = {'x': 100, 'y': 200}
b = a.items ()
print (b)

# Slicing of Tuple
x = ("a", "b", "c", "d", "e")
print (x[2:4])
