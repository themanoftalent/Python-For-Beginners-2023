try:
    x=int(input("Enter the lower limit for the range:"))
    y=int(input("Enter the upper limit for the range:"))
    for i in range(x,y):
        if(i%2==0):
            print (i)
        elif(x==(y-x)):
            print("no even number in this limit")
except:
    print("Invalid entry")
