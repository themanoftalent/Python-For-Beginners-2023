
def main():
    f= open("coolnames.txt","w+")
    for i in range(10):
         f.write("These are cool names %d\r\n" % (i+1))
    f.close()

    #Open the file back and read the contents
f=open("coolnames.txt", "r")
if f.mode == 'r':
    contents =f.read()
    print (contents)

if __name__== "__main__":
  main()