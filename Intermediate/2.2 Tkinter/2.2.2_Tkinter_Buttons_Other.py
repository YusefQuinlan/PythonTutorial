# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 18:57:37 2020

@author: Yusef Quinlan
"""

# Adding red foreground colour (text colour) with fg and adding width padding
# with padx to a label i.e. adding to the x axis of the grid.
from tkinter import *
Window = Tk()
label1 = Label(Window, text="Some generic text", fg="red", padx=100)
label1.grid(row=0,column=0)
Window.mainloop()

# Adding a blue background to a label with bg
Window = Tk()
label1 = Label(Window, text="Some generic text", fg="red", bg="blue", padx=100)
label1.grid(row=0,column=0)
Window.mainloop()

# Adding height padding with pady i.e. on the y axis of the grid.
Window = Tk()
label1 = Label(Window, text="Some generic text", fg="red", bg="blue", padx=100,
               pady=100)
label1.grid(row=0,column=0)
Window.mainloop()

# changing the font style to 'arial bold' and font size to 35 with font 
# declaration.
Window = Tk()
label1 = Label(Window, text="Some generic text", fg="red", bg="blue", padx=100,
               pady=100, font=("arial bold", 35))
label1.grid(row=0,column=0)
Window.mainloop()

# Making a button that can be clicked but does nothing.
Window = Tk()
label1 = Label(Window, text="Text")
label1.grid(row=0, column=0)
button1 = Button(Window, text="CLICK ME!")
button1.grid(row=0, column=1)
Window.mainloop()

# Defining a function that will later be executed on a clicked button
def click():
    global label1
    label1.configure(text="Button has been clicked!")
    
# adding a defined functions functionality to a button when clicked, via
# use of the command attribute/parameter for a button.    
Window = Tk()
label1 = Label(Window, text="Text")
label1.grid(row=0, column=0)
button1 = Button(Window, text="CLICK ME!", command=click)
button1.grid(row=0, column=1)
Window.mainloop()

# Me experiment to see if global variable was necessary, it wasn't.
def click():
    label1.configure(text="Button has been clicked!")
    
Window = Tk()
label1 = Label(Window, text="Text")
label1.grid(row=0, column=0)
button1 = Button(Window, text="CLICK ME!", command=click)
button1.grid(row=0, column=1)
Window.mainloop()


