# def add(a, b):
#     return a + b
#
#
# def subtract(a, b):
#     return a - b
#
#
# def multiply(a, b):
#     return a * b
#
#
# def divide(a, b):
#     return a / b
#
# print('Choose operation.../n')
# print('1. Addision')
# print('2. Subtraction')
# print('3. Multiplication')
# print('4. Division')
#
# choose = int(input("Secim icin sayi gir (1/2/3/4):"))
# # while choose== 1 and 2 and 3 and 4:
# #     continue
#
# num1 = int(input("Birinci sayiyi gir: "))
# num2 = int(input("ikinci sayiyi gir : "))
#
# if choose == 1:
#    print(num1,"+",num2,"=", add(num1,num2))
#
# elif choose == 2:
#    print(num1,"-",num2,"=", subtract(num1,num2))
#
# elif choose == 3:
#    print(num1,"*",num2,"=", multiply(num1,num2))
#
# elif choose == 4:
#    print(num1,"/",num2,"=", divide(num1,num2))
# else:
#    print("Gecersiz islem")

def add(sayi1, sayi2, topla=None):
    topla=sayi1+sayi2
    assert isinstance (topla,object )
    return topla

def subtract(sayi1, sayi2, cikar=None):
    cikar=sayi1-sayi2
    return cikar

def multiply(sayi1, sayi2, carp=None):
    carp=sayi1*sayi2
    return carp

def divide(sayi1, sayi2, bol=None):
    bol=sayi1/sayi2
    return bol


print("Choose a number to have an operation: 1/2/3/4:")

choice=input('Enter a number :')

number1=int(input('Enter the first number :'))
number2=int(input('Enter the econd number :'))

if choice=='1':
    print(add(number1,number2))

elif choice =='2':
    print (subtract (number1, number2))


elif choice=='3':
    print(multiply(number1,number2))

elif choice =='4':
    print (divide(number1, number2))
else:
    print('invalid operation')