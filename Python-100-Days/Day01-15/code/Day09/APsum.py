try:
    n=int(input("enter limit:"))
    a=int(input("enter starting num:"))
    d=int(input("enter common diff:"))
    sum=(n/2)*((2*a)+(n-1)*d)
    print(sum)
except:
    print("Invalid entry")
