''' Basit bir hesap makinesi'''

# Toplma
def add(x, y):
   return x + y

# cikarma
def subtract(x, y):
   return x - y

# carpma
def multiply(x, y):
   return x * y

# bolme
def divide(x, y):
   return x / y

print("Islem seciniz.")
print("1.Toplama")
print("2.Cikarma")
print("3.Carpma")
print("4.Bolme")

# Girdi al
choice = input("Secim icin sayi gir (1/2/3/4):")
# if choice!= 1 or 2 or 3 or 4:
#     print('gecersiz islem')
# exit()

num1 = int(input("Birinci sayiyi gir: "))
num2 = int(input("ikinci sayiyi gir : "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Gecersiz islem")