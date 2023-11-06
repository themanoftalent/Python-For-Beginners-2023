# def main():
#     f=open('guru.txt',"a+")
#
#     for i in range(2):
#         f.write('Append line %d\r\n' %i+1)
#
#         f.close ()
#
#
# if __name__ == '__main__':
#     main ()

# def main():
#     f = open ('Dosya.txt', 'r')
#
#
#     for data in range (2):
#         f_data = f.read ()
#         print(f_data)
#
# if __name__ == '__main__':
#     main ()


# def main():
#     c = open ('Dosta.txt', 'r')
#
#     if c.mode == "r":
#         abds = c.read ()
#         print (abds)
#
#
# if __name__ == '__main__':
#     main ()

def main():
    d = open ('Dosta.txt', 'r')

    d_data = d.readlines() #bunu readlines cevirelim, read yaparsak yukaridan asagiya dogru yaziyor.
    for dala in d_data:
        print (dala)


if __name__ == '__main__':
    main ()
