#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#
def readfileSong():


    with open('playlist.txt', 'r') as f:
        for lines in f:
            split_files = lines.split(';')

            song_name = split_files[0]
            singer_name = split_files[1]
            duration = split_files[-1]

            # print(song_name,singer_name,duration)

            print('Song is :', song_name)
            print('Singer is :', singer_name)
            print('Duration is :', duration)

readfileSong()