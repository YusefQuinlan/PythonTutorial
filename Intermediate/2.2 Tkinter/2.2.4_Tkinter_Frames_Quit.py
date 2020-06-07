# -*- coding: utf-8 -*-
"""
Created on Mon May 25 17:28:33 2020

@author: Yusef Quinlan
"""
""" Just a regular Window with a frame implemented Notice how the frame doesn't
load. This is because there is nothing in it, it has been created though.
"""
from tkinter import *
Window = Tk()

aFrame = LabelFrame(Window, text="this is a frame", padx = 7, pady = 7)
aFrame.pack(padx= 15, pady = 15)

Window.mainloop()


"""
Notice that this frame is implemented and that the button is inside of it.
"""
from tkinter import *
Window = Tk()

aFrame = LabelFrame(Window, text="this is a frame", padx = 7, pady = 7)
aFrame.pack(padx= 15, pady = 15)
myButton = Button(aFrame, text="first button!")
myButton.pack()


Window.mainloop()


"""
Notice that the only change here is to the padx and pady of the LabelFrame(),
this changes the distance/padding between the Frame and the element inside of
the frame.
"""
from tkinter import *
Window = Tk()

aFrame = LabelFrame(Window, text="this is a frame", padx = 70, pady = 70)
aFrame.pack(padx= 15, pady = 15)
myButton = Button(aFrame, text="first button!")
myButton.pack()


Window.mainloop()



"""
Notice that here the change is the change to the padding of the packing of the
frame, this changes the distance/padding between the frame and the main window
(or whatever the frame is inside of)
"""
from tkinter import *
Window = Tk()

aFrame = LabelFrame(Window, text="this is a frame", padx = 7, pady = 7)
aFrame.pack(padx= 150, pady = 150)
myButton = Button(aFrame, text="first button!")
myButton.pack()


Window.mainloop()



"""
In the following, Buttons have been inserted into the frame, but via use of the
grid insertion method and not the pack insertion method. This is because they
are not at the same level as the window, rather they are inside the frame
and the frame is a kind of window within a window.
"""
from tkinter import *
Window = Tk()

aFrame = LabelFrame(Window, text="this is a frame", padx = 7, pady = 7)
aFrame.pack(padx= 15, pady = 15)
myButton = Button(aFrame, text="first button!")
myButton.grid(row=0, column=0)
myButton2 = Button(aFrame, text="second button!")
myButton2.grid(row=1, column=1)
myButton3 = Button(aFrame, text="third button!")
myButton3.grid(row=1, column=2)


Window.mainloop()



"""
In the following example, an error will occur, this is because label1 and 
aFrame are at the same level, but are inserted differently into the window.
"""
from tkinter import *
Window = Tk()

aFrame = LabelFrame(Window, text="this is a frame", padx = 7, pady = 7)
aFrame.pack(padx= 15, pady = 15)
myButton = Button(aFrame, text="first button!")
myButton.grid(row=0, column=0)
myButton2 = Button(aFrame, text="second button!")
myButton2.grid(row=1, column=1)
myButton3 = Button(aFrame, text="third button!")
myButton3.grid(row=1, column=2)
label1 = Label(Window, text="aLabel")
label1.grid(row=1,column=1)

Window.mainloop()


"""
In the following example an error will occur, this is because the Button3
is at the same level as the other two Buttons, but has been inserted with pack()
and not with grid().
"""
from tkinter import *
Window = Tk()

aFrame = LabelFrame(Window, text="this is a frame", padx = 7, pady = 7)
aFrame.pack(padx= 15, pady = 15)
myButton = Button(aFrame, text="first button!")
myButton.grid(row=0, column=0)
myButton2 = Button(aFrame, text="second button!")
myButton2.grid(row=1, column=1)
myButton3 = Button(aFrame, text="third button!")
myButton3.pack()


Window.mainloop()



# The following shows use of the quit() function in a button.
from tkinter import *
Window = Tk()

aFrame = LabelFrame(Window, text="this is a frame", padx = 7, pady = 7)
aFrame.pack(padx= 15, pady = 15)
myButton = Button(aFrame, text="first button!")
myButton.grid(row=0, column=0)
myButton2 = Button(aFrame, text="second button!")
myButton2.grid(row=1, column=1)
myButton3 = Button(aFrame, text="QUIT!", command=Window.quit)
myButton3.grid(row=1, column=2)


Window.mainloop()