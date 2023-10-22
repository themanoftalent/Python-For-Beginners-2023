import random

# Generate a Random Number between 0 and 100 and store it as 'numberToguess'
numberToGuess = random.randint(0, 5)

userGuess = 0

while userGuess != numberToGuess:
    # Get the user to enter a number using the 'input' function and convert in to an Integer suing the 'int' function
    userGuess = int(input("Guess the number (between 1 and 1000)"))

    # Compare this number, userGuess, with the numberToGuess - Display the right message if the userGuess is greater than, lower than or equal to the numberToGuess
    if userGuess > numberToGuess:
        print("Too high!")
    elif userGuess < numberToGuess:
        print("Too low!")
    elif userGuess == numberToGuess:
        print("Good guess, the number to guess was " + str(numberToGuess) + " indeed.")
        # End of game - exit the while loop
        break