
#  !/usr/bin/python
#  Copyright (c) akifciftci 2019. Aim to help new beginner to try hard and learn more.
#

salary = float(input('Revenue for the month: '))
insurance = float(input('insurances: '))

diff = salary - insurance - 4500
if diff <= 0:
    rate = 0
    deduction = 0

elif diff < 1800:
    rate = 0.03
    deduction = 0

elif diff < 5500:
    rate = 0.1
    deduction = 105

elif diff < 10000:
    rate = 0.2
    deduction = 555

elif diff < 45000:
    rate = 0.25
    deduction = 1005

elif diff < 65000:
    rate = 0.3
    deduction = 2755

elif diff < 90000:
    rate = 0.35
    deduction = 5505

else:
    rate = 0.45
    deduction = 13505

tax = abs(diff * rate - deduction)
print('Income: %.2f' % tax)
print('Actual Income: %.2f' % (diff + 3500 - tax))
