# -*- coding: utf-8 -*-
"""
Created on Tue May 26 16:48:09 2020

@author: Yusef Quinlan
"""

#Making a generic window
from tkinter import *
Window = Tk()

Window.mainloop()


"""
A generic window has been made, and a second window with title 'window2' has 
been created by assigning the function Toplevel() to the Window2 variable,
the title is then applied to this variable. A label has been added to the 
Toplevel() created window. When this example is run, 2 windows can be seen,
the main window and the created Window2. If the main window is closed, the
mainloop() will be exited, however Toplevel() Windows as they are do not close
mainloop() when they are closed. So if you close Window2, the main window will
still be open and the mainloop() will continue running.
"""
from tkinter import *
Window = Tk()
Window.title("Main window")

Window2 = Toplevel()
Window2.title("Window2")
Label(Window2, text="this is a label").pack()

Window.mainloop()


"""
In the following, two Toplevel() windows have been created, this demonstrates
that several Toplevel() windows can exist at the same time.
"""
from tkinter import *
Window = Tk()
Window.title("Main window")

Window2 = Toplevel()
Window2.title("Window2")
Label(Window2, text="this is a label").pack()

Window3 = Toplevel()
Window3.title("Window3")
Label(Window3, text="Window 3's label").pack()

Window.mainloop()



"""
This last example shows that windows can be made via functions, i.e. 
functions placed in buttons, however the button can be click several times to 
create several windows.
"""
from tkinter import *
Window = Tk()
Window.title("Main Window")

def newWindow():
    newWindow = Toplevel()
    Label(newWindow, text="eejrfherhfrek").pack()


Button(Window, text="Make a new window!", command=newWindow).pack()
Window.mainloop()