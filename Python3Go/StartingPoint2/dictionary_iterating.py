Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963,
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}

for album_title in Beatles_Discography:
    print("Title: {}, year: {}".format(album_title, Beatles_Discography[album_title]))
print('*'*23)
def most_prolific(discs):
#We will store a dictionary of years
#and number of albums per year
    years = {}
    maxyears = []
    maxnumber = 0
    for disc in discs:
        year = discs[disc]
        if year in years:
            years[year] += 1
        else:
            years[year] = 1

#find the year in which the maximum
#number of albums was published
#there are more elegant ways of accomplishing this,
#but the code below works
    for year in years:
        if years[year] > maxnumber:
            maxyears=[]
            maxyears.append(year)
            maxnumber = years[year]
        elif years[year] == maxnumber and not (year in maxyears):
            maxyears.append(year)
    if (len(maxyears) == 1):
        return maxyears[0]
    else:
        return maxyears