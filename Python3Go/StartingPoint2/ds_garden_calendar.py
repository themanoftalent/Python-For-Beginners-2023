def garden_calendar(season):
    if season == "spring":
        print ("time to plant the garden!")
    elif season == "summer":
        print ("time to water the garden!")
    elif season == "autumn" or season == "fall":
        print ("time to harvest the garden!")
    elif season == "winter":
        print ("time to stay indoors and drink tea!")
    else:
        print ("I don't recognize that season")


#garden_calendar("spring") #we have to call the function
garden_calendar(input("Enter your favorite season :"))

