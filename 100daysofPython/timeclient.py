##################################################
#### **************************************** ####
#### !/usr/bin/python3                        ####
#### -*- coding: utf-8 -*-                    ####
#### @Time    : 2023/20/10 11:40              ####
#### @Author  : themanoftalent                ####
#### @Site:https://github.com/themanoftalent  ####
#### @Project : python-app                    ####
#### **************************************** ####
##################################################


from socket import socket


def main():
    client = socket()
    client.connect(('10.7.152.69', 6789))
    print(client.recv(1024).decode('utf-8'))
    client.close()


if __name__ == '__main__':
    main()
