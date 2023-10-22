myseq = [["ab"], "b", [["c", "d"], "e",],"f"]
def getList(seq):
    newstring = ""
    for i in seq:
        if type(i) is str:
            newstring += i
        else:
            newstring += getList(i)
    return newstring
print getList(myseq)
