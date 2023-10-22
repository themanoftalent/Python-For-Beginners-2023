try:
    n=int(input("enter the number"))
    x=int(input("enter the power"))
    if(x==0):
        print("1")
    elif(n==0):
        print("0")
    else:
        print(n**x)
except:
    print("Invalid entry")
