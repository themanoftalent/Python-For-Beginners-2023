mystring = "rat"

def checkP(inString):
    mydict = {}
    counter = 0
    for i in inString:
        if i in mydict:
            if mydict[i] ==2:
                mydict[i] = 1
            else:
                mydict[i] = 2
                counter += 2
        else:
            mydict[i] = 1
    print counter
    print len(inString)
    if len(inString) - 1 == counter:
        return True
    else:
        return False
print checkP(mystring)


def hasPalindrome(the_string):
    unpaired = set()

    for char in the_string:
        if char in unpaired:
            unpaired.remove(char)
        else:
            unpaired.add(char)
    return len(unpaired) <= 1
