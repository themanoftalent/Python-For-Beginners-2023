'''Python provides various options for developing graphical user interfaces (GUIs).
Most important are listed below.

1. Tkinter − Tkinter is the Python interface to the Tk GUI toolkit shipped with Python. We would look this option in this chapter.

2. wxPython − This is an open-source Python interface for wxWindows http://wxpython.org.

3. JPython − JPython is a Python port for Java which gives Python scripts seamless access to Java class
   libraries on the local machine http://www.jython.org.

====================================================================================================================================
Tkinter Programming

Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications.
Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.

Creating a GUI application using Tkinter is an easy task. All you need to do is perform the following steps −

    Import the Tkinter module.

    Create the GUI application main window.

    Add one or more of the above-mentioned widgets to the GUI application.

    Enter the main event loop to take action against each event triggered by the user.

Example

#!/usr/bin/python

import tkinter
top = tkinter.Tk()
# Code to add widgets will go here...
top.mainloop()

This would create a following window −
TK Window
'''
'''\
from tkinter import Tk, Label, Button

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()



'''

from tkinter import *

root = Tk()


##Label(root, text="This is a label").pack()

# Button(root, text="This is a button").pack()

def name():
    print("My name is Canan")


f = Frame(root)

Label(f, text="Hello").pack()
Button(f, text="Greetings", command=name()).pack()
f.pack()
root.mainloop()
