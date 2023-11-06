#ab address boook.
ab = {
    'ali bakal': 'alibakal@gmail.com', 'mehmet cemal': 'mehmetcemal@hotmail.com',
    'emir kaan': ' emirkaan@yahoo.com', 'enis kara': 'eniskara@yandex.com',
    'Swaroop jane': 'swaroop@swaroopch.com', 'Larry Kanda': 'larry@wall.org',
    'Matsumoto duo': 'matz@ruby-lang.org', 'Spammer hana': 'spammer@hotmail.com' #arada nokta bulunacak
}

print ("Ali is in address book", ab['ali bakal'])
print ("There are {} cotacts in address book." .format(len(ab)) ,
       "Another way of printing the length of address book : ", len (ab))

"""deleting a key value"""
del ab['Spammer hana']

print ("\nThere are {} cotacts in address book after deleting a contact." .format(len(ab)))
print('++'*25)
print("Printing all names and addresses\n\t")
for name, address in ab.items():
 print('Contact {} at {}'.format(name, address))
print('++'*25)
"""Adding a key-value pair"""
ab['Cengiz Hakan '] = 'cengizhakan@python.org'
print("\nChecking if :")
if 'Guido' in ab:
     print("\nGuido's address is", ab['Guido'])
else:
        'Cengiz Hakan' in ab
        print(True)

print('++'*25)

print ("All names and address is address book : \n")

for a,b in ab.items():
    print(a,b)