def main():
    a=input("enter a number=")
    try:
     x=int(a)%2
     if(int(x)==0):
        print(a+" is even")
     else:
        print(a+" is odd")
    except:
        print("invalid entry")
if __name__ == '__main__':
    main()
