n=input("Enter the limit=")
try:
    n=int(n)
    s=int(n*(n+1)/2)
    print(s)
except:
    print("Invalid Entry")
