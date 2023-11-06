try:
    n=int(input("Enter max elements in array:"))
    if(n>1000):
        print("more than 1000")
    a=[int(input()) for i in range(n)]
    list.sort(a)
    print(*a)
except:
    print("Invalid entry")
