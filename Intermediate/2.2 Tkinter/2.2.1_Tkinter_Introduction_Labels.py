# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 13:35:13 2020

@author: Yusef Quinlan
"""

# What is Tkinter?
# Essentially Tkinter is used to make User interfaces or Graphical user interfaces

from tkinter import *

# Making a tkinter window with Tk(), adding a title to it and running it.
Window = Tk()
Window.title("First Tkinter Window")
#Window.mainloop()

# Adding a label to our window.
Label1 = Label(Window, text="First label")
Label1.pack()
#Window.mainloop()

# Here we add a label but assign it a grid position in the window.
Window = Tk()
Window.title("First Tkinter Window")
Label1 = Label(Window, text="First label")
Label1.grid(row=0, column=0)
Window.mainloop()

# Here multiple labels are added and each is assigned a distinct grid position
Window = Tk()
Window.title("First Tkinter Window")
Label1 = Label(Window, text="First label")
Label1.grid(row=0, column=0)
Label2 = Label(Window, text="My name is Yusef")
Label2.grid(row=1, column=1)
Label3 = Label(Window, text="Hello world!")
Label3.grid(row=2, column=2)
Window.mainloop()

"""
 This shows that grid positions are relative, we might expect that Label2 
 would be 6 column and row positions away from Label1, but instead it is only
 1 row and column apart. This is because 7 is taken as the max value so far
 and the next highest position is 1 position away from Label1, relative to
 Label1, Label2 is the maximum current distance from Label1.
"""

Window = Tk()
Window.title("First Tkinter Window")
Label1 = Label(Window, text="First label")
Label1.grid(row=0, column=0)
Label2 = Label(Window, text="My name is Yusef")
Label2.grid(row=7, column=7)
Window.mainloop()

# Further demonstration of relative positioning, look at where label3 is...
Window = Tk()
Window.title("First Tkinter Window")
Label1 = Label(Window, text="First label")
Label1.grid(row=0, column=0)
Label2 = Label(Window, text="My name is Yusef")
Label2.grid(row=1, column=1)
Label3 = Label(Window, text="Hello world!")
Label3.grid(row=3, column=3)
Window.mainloop()