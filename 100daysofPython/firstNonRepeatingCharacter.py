#Given a string s consisting of lowercase Latin Letters, find the 
#first non repeating character in s.

theString = "hello"
theString = "zxvczbtxyzvy"

def findUnique(theString):
	mydict = {}
	for i in theString:
		if i not in mydict:
			mydict[i] =1
		else:
			mydict[i] += 1
	for i in mydict:
		if mydict[i] == 1:
			print i
			break
findUnique(theString)
