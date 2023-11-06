#edited for python 3 and some basic arrangments
#!editor :Barish

def passFun():
    print ('abc')
    pass
    i=0
    while True:
        if i==1000: #break added
            break
        print ('loop', i)
        i += 1
        pass


passFun();
