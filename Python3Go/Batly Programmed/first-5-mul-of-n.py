try:
    n=int(input("Enter a number:"))
    x=1
    for i in range (1,6):
        x=n*i
        print(x)
except:
    print("Invalid Entry")
