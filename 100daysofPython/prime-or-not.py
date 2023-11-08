try:
    num = int(input("Enter a number: "))
    if(num>1000):
        print("enter less than 1000")
    elif num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print("no")
                break
        else:
            print("yes")
    else:
        print("no")
except:
    print("Invalid Entry")
