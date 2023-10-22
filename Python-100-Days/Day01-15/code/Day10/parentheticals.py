"""

Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."

Write a function that, given a sentence like the one above, along with the position of an opening parenthesis, finds the corresponding closing parenthesis.

Example: if the example string above is input with the number 10 (position of the first parenthesis), the output should be 79 (position of the last parenthesis).


"""
mystring = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
def getClosing(yourString,number):
        counter = 0
	for indx, val in enumerate(yourString):
            if indx > number:
                if val =="(":
                    counter += 1
                elif val==")":
                    counter -=1
                if counter == -1:
                    return indx
        raise Exception("Error: no closing parenthesis")
	
print getClosing(mystring, 10)

	
