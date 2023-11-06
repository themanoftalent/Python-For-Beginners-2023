#! /usr/bin/python

while True:
    guess = raw_input("please input a string: ")
    if guess == 'quit':
        break
else:
    print('Done in else statement') # else will never excute because when exit it excute break, and it will never goes to else-statment
print('Done not excuting else statment using break')
