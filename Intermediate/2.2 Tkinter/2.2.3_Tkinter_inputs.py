# -*- coding: utf-8 -*-
"""
Created on Sun May 17 12:41:29 2020

@author: Yusef Quinlan
"""
# Setting up the general window and adding functionality to a label.
from tkinter import *
Window = Tk()

def onClick():
    aLabel = Label(Window, text="You've clicked our button!")
    aLabel.grid(row=2, column=0)

aButton = Button(Window, text="Click the button!", command=onClick)
aButton.grid(row=1, column=0)

Window.mainloop()


"""
In addition to the regular setup, an Entrywidget (or an input box) has been
added to the Window, this allows users to type in an input.
However this input is not taken from the input box and so is unused in the
following example.
"""
from tkinter import *
Window = Tk()
inputwidget = Entry(Window)
inputwidget.grid(row=0,column=0)

def onClick():
    aLabel = Label(Window, text="You've clicked our button!")
    aLabel.grid(row=2, column=0)

aButton = Button(Window, text="Click the button!", command=onClick)
aButton.grid(row=1, column=0)

Window.mainloop()



"""
Here the Entrywidget/inputbox input has been taken with the .get() function,
this function is applied to an entry widget in the following manner
Entrywidgetvarname.get()    

But the recieved input is not used at any point so is useseless in this example
"""
from tkinter import *
Window = Tk()
inputwidget = Entry(Window)
inputwidget.grid(row=0,column=0)
inputwidget.get()

def onClick():
    aLabel = Label(Window, text="You've clicked our button!")
    aLabel.grid(row=2, column=0)

aButton = Button(Window, text="Click the button!", command=onClick)
aButton.grid(row=1, column=0)

Window.mainloop()

"""
In the following example the Entrywidget.get() function is used in the onClick()
function as defined below and is added to the text of a label created by the 
function. The function itself is a litle buggy, but don't worry about that, 
this is just to demonstrate that the .get() can be used, the returned data from
.get() could also be stored in a variable.

"""
from tkinter import *
Window = Tk()
inputwidget = Entry(Window)
inputwidget.grid(row=0,column=0)

def onClick():
    aLabel = Label(Window, text="You've clicked our button! " + inputwidget.get())
    aLabel.grid(row=2, column=0)

aButton = Button(Window, text="Click the button!", command=onClick)
aButton.grid(row=1, column=0)

Window.mainloop()



"""
The following example just shows that certain properties such as width and
bg (background colour) and fg (foreground colour) can be added to an EntryWidget
It shows nothing else.
"""
from tkinter import *
Window = Tk()
inputwidget = Entry(Window, fg="red", bg="blue", width=55)
inputwidget.grid(row=0,column=0)

def onClick():
    aLabel = Label(Window, text="You've clicked our button! " + inputwidget.get())
    aLabel.grid(row=2, column=0)

aButton = Button(Window, text="Click the button!", command=onClick)
aButton.grid(row=1, column=0)

Window.mainloop()