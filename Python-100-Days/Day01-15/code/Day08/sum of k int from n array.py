try:
    n=int(input("enter no. of terms"))
    i=0
    a=[int(input()) for i in range(0,n)]
    k=int(input("Enter no of terms to be added:"))
    s=0
    i=0
    while(i<k):
        s=int(s)+a[i]
        i=i+1
    print("sum of integers is:"+str(s))
except:
    print("Invalid Entry")
