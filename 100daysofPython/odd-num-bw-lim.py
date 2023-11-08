try:
    x=int(input("Enter the lower limit for the range:"))
    y=int(input("Enter the upper limit for the range:"))
    for i in range(x+1,y):
        if(i%2!=0):
            print (+i)
    print("no odd number in this limit")
except:
    print("Invalid entry")
