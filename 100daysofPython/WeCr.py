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

import tkinter as tk

def display_text():
    label.config(text="Bir Akif Cifci Hikayesi yaziyorum. Figuran olma. Başrol OL.")


root = tk.Tk()
root.title("Click Me")
root.geometry("400x400+400+100")  


label = tk.Label(root, text="Click Me")
label.pack(pady=20)

button = tk.Button(root, text="Click Me", command=display_text)
button.pack()

root.mainloop()
