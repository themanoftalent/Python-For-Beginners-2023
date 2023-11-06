try:
    x=int(input("Enter the lower limit for the range:"))
    y=int(input("Enter the upper limit for the range:"))
    if((y-x)==1):
        print("no prime number in this limit")
    for n in range(x,y):
        if(n>1):
            for i in range(2,n):
                if(n%i==0):
                    break
            else:
                print(n)
except:
    print("Invalid entry")
