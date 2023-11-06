# import sys
# import random
#
# def gameGueess():
#
#     guess=0
#     number=random.randint(1,40)
#
#     print('Enter a number')
#
#     while True:
#         try:
#             secretNumber=int(input('Enter your secret number'))
#
#             if secretNumber==number:
#                 print('you win')
#                 guess+=1
#                 break
#
#             elif secretNumber>number:
#                 print('high')
#                 guess=guess+1
#
#             elif secretNumber<number:
#                 print('Too low')
#                 guess+=1
#
#         except ValueError:
#             print('Not a number')
#             continue
#             print('')
#
# gameGueess()
# wannaplay=str(input('Enter y to continue'))
#
# if wannaplay=='y':
#     gameGueess()
# else:
#     sys.exit()

import random
import sys


def guessing_game():
    number = random.randint (1, 5500)
    guess = 0

    print ('Enter a number between 1-5500 \n')

    while True:
        try:
            luckynumber = int (input ('Enter a number :'))
            if luckynumber == number:
                print ('Correct you have done ')
                guess += 1
                break
            elif luckynumber > number:
                print ('Your guess is a little higher ')
                guess += 1
            elif luckynumber < number:
                print ('Your guess is a lower ')
                guess += 1
        except ValueError:
            print ('It is not a whole number, try again')
            continue
            print ('Your guess is ', guess, 'guess')


guessing_game ()
play_again = str (input ('Enter y for continuing or n to quit '))

if play_again == 'y':
    guessing_game ()
else:
    sys.exit
