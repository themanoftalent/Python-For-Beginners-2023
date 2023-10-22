def main():
    a=input("Enter First Number=")
    b=input("Enter Second Number=")
    c=input("Enter Third Number=")
    try:
      if(int(a)>int(b)):
        x=a
      else:
        x=b
      if(int(x)>int(c)):
        print(x+" is the largest number")
      else:
        print(c+" is the largest number")
    except:
        print("invalid entry")
if __name__ == '__main__':
    main()
