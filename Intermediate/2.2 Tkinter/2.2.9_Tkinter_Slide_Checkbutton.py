# -*- coding: utf-8 -*-
"""
Created on Tue May 26 20:08:41 2020

@author: Yusef Quinlan
"""

"""
Demonstrating the use of a slider with the Scale() creator. Note that scales
or sliders should be packed on a different line to the line they are created on.
Also the from_ parameter has an underscore and dictates the lowest value and to
dictates the highest value of the slider.
"""
from tkinter import *
Window = Tk()
Window.title("Main Window")

defaultVert = Scale(Window, from_=0, to=20)
defaultVert.pack()

Window.mainloop()


# Sliders can be made horizontal with the orient=HORIZONTAL parameter, note
# that HORIZONTAL is all capitals.
from tkinter import *
Window = Tk()
Window.title("Main Window")

defaultVert = Scale(Window, from_=0, to=20)
defaultVert.pack()

Hori = Scale(Window, from_=0, to=10, orient=HORIZONTAL)
Hori.pack()

Window.mainloop()

# An example of sliders values being gotten with .get() in a function.

from tkinter import *
Window = Tk()
Window.title("Main Window")

def horiget():
    Label(Window, text=Hori.get()).pack()

defaultVert = Scale(Window, from_=0, to=20)
defaultVert.pack()

Hori = Scale(Window, from_=0, to=10, orient=HORIZONTAL)
Hori.pack()

Button(Window, text="Get the value of Hori", command=horiget).pack()
Window.mainloop()


"""
A checkbutton is made with the Checkbutton() constructor. It needs to be 
assigned a variable to it, of type IntVar(), this is because by default its
value is either a 1 or a 0, 1 if checked and 0 if not checked.
"""
from tkinter import *
Window = Tk()
Window.title("Main Window")

var = IntVar()
defCheck = Checkbutton(Window, text="generic checkbutton", variable=var)
defCheck.pack()

Window.mainloop()


# the value can be gotten with .get()
from tkinter import *
Window = Tk()
Window.title("Main Window")

def check():
    print(var.get())

var = IntVar()
defCheck = Checkbutton(Window, text="generic checkbutton", variable=var)
defCheck.pack()

Button(Window, text="value of checkbutton", command=check).pack()

Window.mainloop()


"""
Here we can see that the default values have beeen changed to strings using the
onvalue and offvalue parameter, the onvalue value is the value when the 
checkbox is checked and the offvalue value is the value when the checkbox is
unchecked. We can assign these to be Strings and therefore change our tkinter
variable to be of type StringVar if we wish.

"""
from tkinter import *
Window = Tk()
Window.title("Main Window")

def check2():
    print(var2.get())

var2 = StringVar()
defCheck2 = Checkbutton(Window, text="generic checkbutton", variable=var2,
                        onvalue="Checked", offvalue="Not-Checked")
defCheck2.pack()

Button(Window, text="value of checkbutton", command=check2).pack()

Window.mainloop()


"""Weird errors can occur when sliders are checked by default, use the 
.deselect() function on a checbox/checkbutton so that it is deselected
or unchecked by default.
"""
from tkinter import *
Window = Tk()
Window.title("Main Window")

def check2():
    print(var2.get())

var2 = StringVar()
defCheck2 = Checkbutton(Window, text="generic checkbutton", variable=var2,
                        onvalue="Checked", offvalue="Not-Checked")
defCheck2.pack()
defCheck2.deselect()

Button(Window, text="value of checkbutton", command=check2).pack()

Window.mainloop()