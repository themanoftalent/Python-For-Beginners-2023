try:
    x=int(input("Enter a number:"))
    fact=1
    for i in range (1,x+1):
        fact=fact*i
    print(fact)
except:
    print("Invalid Entry")
