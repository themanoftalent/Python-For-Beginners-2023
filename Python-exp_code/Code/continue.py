#! /usr/bin/python
# Filename: 3.continue.py
while True:
    guess = raw_input("please input a string: ")
    if guess == 'quit':
        break
    if len(guess) < 3:
        continue
    print("sufficient length >= 3")
else:
    print('else statment')
print("Over")
