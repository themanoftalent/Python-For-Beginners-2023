# # # class takeAvrg_class:
# # #     def defAvrg(a, b, c):  # get the defAvrg of three numbers
# # #         take_result = a + b + c
# # #         result = take_result / 3
# # #         return result
# # #
# # #
# # # # now use the function defAvrg from the takeAvrg_class class
# # # x = takeAvrg_class.defAvrg(9, 18, 27)
# # #
# # # p

# class my_class(object):
#     def __init__(self, number1, number2, number3):
#         self.number1 = number1
#         self.number2 = number2
#         self.number3 = number3
#
#     def defAvrg(self):  # get the defAvrg of three numbers
#         return  (self.number1 + self.number2 + self.number3)/3
#         #resulin = resulted / 3
#         #return resulted
#
# number1 = 10
# number2 = 20
# number3 = 30
# my_class2 = my_class(numbers = [float(input("Enter number %s: "%i)) for i in range(3)])
# print(my_class2.defAvrg())


# ========================================================
# numbers = list()
# for i in range(0, 3):
#     inputNr = int(input("Enter a number: "))
#     if(inputNr == -99):
#         break
#
#     numbers.append(inputNr)
#
# #Then we take all of the numbers and calculate the sum and avg on them
# sum = 0
# for j, val in enumerate(numbers):
#     sum += val
#
# print("The total sum is: " + str(sum))
# print("The avg is: " + str(sum / len(numbers)))


# from statistics import mean
#
# class my_class(object):
#     def __init__(self, numbers):
#         self.numbers = numbers
#
#     def defAvrg(self):
#         return mean(self.numbers)
#
# my_class2 = my_class(*[float(input("Enter number %s: "%i)) for i in range(3)])
# print(my_class2)


# ======================

# num = int(input('How many numbers: '))
# total_sum = 0
#
# for n in range(num):
#     numbers = float(input('Enter number : '))
#     total_sum += numbers
#
# avg = total_sum/num
# print('Average of ', num, ' numbers is :', avg)

sayi = int(input('Kac tane sayi girmek ister : '))
toplam_sayi = 0

for i in range(sayi):
    girilen = float(input('Enter numbers : '))
    toplam_sayi += girilen

averaj = toplam_sayi / sayi
print(averaj)
