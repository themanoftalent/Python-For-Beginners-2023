try:
    n=int(input("Enter max elements in array:"))
    if(n>1000):
        print("more than 1000")
    a=[int(input()) for i in range(n)]
    list.sort(a)
    print(*a)
    m=len(a)//2
    print(a[m])
except:
    print("Invalid entry")
