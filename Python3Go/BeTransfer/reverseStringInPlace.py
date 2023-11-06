#reverse a string in place
def reverse(string):
    mylist = list(string)
    b = ""
    sizeL = len(mylist)
    for indx,val in enumerate(mylist):
        if indx >= sizeL/2:
            b = mylist[sizeL-1-indx]
            mylist[sizeL-1-indx] = mylist[indx]
            mylist[indx] =  b
        
    print mylist
reverse("hellow")
