import random
import _random

def playGuess():
    print ('Type a number betwen 1-100 ')

    number =random.randint(1,101)
    guess = 0

    while number!=guess:
        print()
        if number>guess:
            print('too gigh')
            guess+=1
        elif number<guess:
            print('too low')
            guess+=1
        else:
            print('Enter an int')
            break




playGuess()

