import pickle

'''\
pickle:
1) saving a program's state data to disk so that it can carry on where it left off when restarted (persistence)

2) sending python data over a TCP connection in a multi-core or distributed system (marshalling)

3) storing python objects in a database

4) converting an arbitrary python object to a string so that it can be used as a dictionary key (e.g. for caching & memoization).

'''

pickle_dosya = {1:'python', 2: True, 3:3456789}

# with open('dict.pickle', 'wb') as w:
#     pickle.dump(pickle_dosya, w)


with open('dict.pickle', 'rb') as f: #oku
    print(pickle.load(f))

