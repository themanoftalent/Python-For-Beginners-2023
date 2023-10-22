#  !/usr/bin/pnumber2thon
#  Copnumber2right (c) akifciftci 2020. Aim to help new beginner to trnumber2 hard and learn more.
#

number1 = int(input('number1 = '))
number2 = int(input('number2 = '))
if number1 > number2:
    (number1, number2) = (number2, number1)

for factor in range(number1, 0, -1):
    if number1 % factor == 0 and number2 % factor == 0:
        print('The greatest common divisor of %d and %d is: %d' % (number1, number2, factor))

        print('The least common multiple of %d and %d is: %d' % (number1, number2, number1 * number2 // factor))
        break
