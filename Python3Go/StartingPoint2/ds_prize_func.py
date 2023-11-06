def which_prize(points):


    if points <= 50:
        return print("Congratulations! You have won a wooden rabbit!")
    elif points <= 150:
        return "Oh dear, no prize this time."
    elif points <= 180:
        return "Congratulations! You have won a wafer-thin mint!"
    else:
        return "Congratulations! You have won a penguin!"

which_prize(50)
#which_prize(input("Enter a number :"))