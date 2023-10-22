phone_book = {"John": 123, "Jane": 234, "Jerard": 345}  # create new dictionary
print(phone_book)

# Add new item to the dictionary
phone_book["Jill"] = 456
print(phone_book)


print()
print(phone_book.keys())

print(phone_book.values())
print()
for i in phone_book.keys():
    print(i)
print('values')
for i in phone_book.values():
    print(i)
