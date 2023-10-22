def main():
    x=input("Enter a alphabet=")
    try:
     y=['a','e','i','o','u','A','E','I','O','U']
     if(str(x) in y):
        print(x+" is vowel")
     else:
        print(x+" is consonant")
    except:
        print("invalid entry")
if __name__ == '__main__':
    main()
