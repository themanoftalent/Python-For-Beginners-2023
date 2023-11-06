def main():
    f= open("guru99.txt","w+")
    f=open("guru99.txt","a+")
    for i in range(10):
         f.write("This is line %d\r\n" % (i+1))
    f.close()
    #Open the file back and read the contents
    f=open("guru99.txt", "r")
    if f.mode == 'r':
       contents =f.read()
    print (contents)
if __name__== "__main__":
  main()