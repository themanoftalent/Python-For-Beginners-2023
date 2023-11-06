with open ('test1.txt', 'r') as f: #test1.txt ayri bir dosya olarak yanda 
    reado = open ('test1.txt', 'r')
    size_to_read = 30
    f_contents = f.read (size_to_read)
    while len (f_contents) > 0:
        print (f_contents)
        f_contents = reado.read (size_to_read)
