def wordcounter(filename):
    try:
        fp = open(filename)
        fc = fp.read()
    except:
        print('File IO Problem has been occured.')
        return

        fp.close()

        word_count = dict()

        word_list = fc.split()

for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for key in word_count:
    if word_count[key] == 1:
        print(str(filename) + " has " + str(word_count[key]) + " time " + key)
    else:
        print(str(filename) + ' has ' + str(word_count[key]) + ' times ' + key)

wordcounter('“emre.txt”')