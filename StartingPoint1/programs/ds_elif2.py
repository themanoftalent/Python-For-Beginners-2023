# First Example
bakiye = 5.68
banka_hesap = 1049.19
# bakiye = 15.68 and  banka_hesap = 1039.19
if bakiye < 10:
    bakiye += 10
    banka_hesap -= 10
print ('Bakiyeniz', bakiye)
print ('Banka hesabiniz ', banka_hesap)
print ('--' * 23)

# Second Example

sayi = 5  # sayi = 5 %2= 3 remain
if sayi % 2 == 0:
    print ("Bu sayi " + str (sayi) + " ciftir.")
else:
    print ("Bu sayi " + str (sayi) + " tektir.")

print ('--' * 23)

#2.1 example

sayim = int(input('Bir sayi giriniz :'))  # sayi = 5 %2= 3 remain
if sayim % 2 == 0:
    print ("Bu sayi " + str (sayim) + " ciftir.")
else:
    print ("Bu sayi " + str (sayim) + " tektir.")

print ('--' * 23)



# Third Example
# change  age to experiment with  pricing

age = 35

# set  age limits for bus fares
cocuk_bedava = 6
ogrenci = 18
emekli = 65

# set bus fares
concession_ticket = 1.25
adult_ticket = 2.50

# ticket price logic
if age <= cocuk_bedava:
    bilet_ederi = 0
elif age <= ogrenci:
    bilet_ederi = concession_ticket
elif age >= emekli:
    bilet_ederi = concession_ticket
else:
    bilet_ederi = adult_ticket
message = "{} yasinda olan birisi  {} TL. para odeyecek.".format (age, bilet_ederi)
print (message)
