with open ('test1.txt', 'r') as f:
    f_contents = f.read ()
    size_to_read = 100
    nano_to_read = 0

    while len (f_contents) > nano_to_read:
        print (f_contents)
        f_contents = f.read (size_to_read)
