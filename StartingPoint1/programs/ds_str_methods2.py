names = "Akifhan"
if "n" in names:
    print ('Yes there is n')
if names.startswith ("A"):
    print ('True, it starts with A')

if names.find ('han') != -1:
    print ('Akifhan names contain han')
print ('\n')
#listeyi birlestir man
delimeter = '_*_'
myList=['Russia','Brasil,England','Enemeies','Big Picture']
print(delimeter.join(myList))
