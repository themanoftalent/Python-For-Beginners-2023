a=0
try:
    if a==0:raise ValueError("a should not be zero")
    c=29/a
    print(c)
except ValueError as e:
    print(e)
print("normal flow")