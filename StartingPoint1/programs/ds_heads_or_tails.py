import random

count = 0
while count < 20:
    count += 1

para = random.randrange (2)

if para == 1:
    print ('Tura')
else:
    print ('Yazi')

print ('A little more advanced : \n')


flips = 1
coin = random.randint (1, 2)
heads = 0
tails = 0

while flips <= 10:
    if coin == 1:
        print ("Heads")
        heads += 1
        flips += 1
    elif coin == 2:
        print ("tails")
        tails += 1
        flips += 1

print ("You got", heads, "heads and", tails, "tails!")

input ("Exit")
