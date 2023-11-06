def total(a=5, *numbers, **phonebook):
    print('a sayisi', a)
    print('-'*34)
    #iterate through all the items in tuple
    for single_item in numbers:
        print('single_item', single_item)
        
    #iterate through all the items in dictionary    
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)

print(total(55,1,2,3,'\n',Jack=44401123,John=5552231,Inge=3331560))
