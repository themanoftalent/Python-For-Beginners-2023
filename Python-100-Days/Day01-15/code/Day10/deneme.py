numbers = list()
for i in range(0, 3):
    inputNr = int(input("Enter a number: "))
    if(inputNr == -99):
        break

    numbers.append(inputNr)

#Then we take all of the numbers and calculate the sum and avg on them
sum = 0
for j, val in enumerate(numbers):
    sum += val

print("The total sum is: " + str(sum))
print("The avg is: " + str(sum / len(numbers)))


num = int(input('How many numbers: '))
total_sum = 0

for n in range(num):
    numbers = float(input('Enter number : '))
    total_sum += numbers

avg = total_sum/num
print('Average of ', num, ' numbers is :', avg)
