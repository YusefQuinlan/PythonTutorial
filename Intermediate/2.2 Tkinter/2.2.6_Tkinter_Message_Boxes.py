# -*- coding: utf-8 -*-
"""
Created on Tue May 26 15:26:44 2020

@author: Yusef Quinlan
"""

"""
The following example shows how a messagebox can be created, the box
is created by the Button when it is clicked as the function msgbox is called
and within this function a messagebox is created with the messagebox.type() 
function is called. The messagebox created is a showinfo box.
"""
from tkinter import *
Window = Tk()
Window.title("Message Box")

def msgbox():
    messagebox.showinfo("Title","Message")

Button(Window, text="MsgBox", command=msgbox).grid(row=0, column=0)
Window.mainloop()

# showinfo, showwarning, showerror, askquestion, askyesno, askokcancel

#the following just creates a showwarning messagebox
from tkinter import *
Window = Tk()
Window.title("Message Box")

def msgbox():
    messagebox.showwarning("Title","Message")

Button(Window, text="MsgBox", command=msgbox).grid(row=0, column=0)
Window.mainloop()

# showinfo, showwarning, showerror, askquestion, askyesno, askokcancel


#the following just creates a showerror messagebox
from tkinter import *
Window = Tk()
Window.title("Message Box")

def msgbox():
    messagebox.showerror("Title","Message")

Button(Window, text="MsgBox", command=msgbox).grid(row=0, column=0)
Window.mainloop()

# showinfo, showwarning, showerror, askquestion, askyesno, askokcancel


#the following just creates an askquestion messagebox
from tkinter import *
Window = Tk()
Window.title("Message Box")

def msgbox():
    messagebox.askquestion("Title","Message")

Button(Window, text="MsgBox", command=msgbox).grid(row=0, column=0)
Window.mainloop()

# showinfo, showwarning, showerror, askquestion, askyesno, askokcancel


#the following just creates an askyesno messagebox
from tkinter import *
Window = Tk()
Window.title("Message Box")

def msgbox():
    messagebox.askyesno("Title","Message")

Button(Window, text="MsgBox", command=msgbox).grid(row=0, column=0)
Window.mainloop()

# showinfo, showwarning, showerror, askquestion, askyesno, askokcancel



#the following just creates an askokcancel messagebox
from tkinter import *
Window = Tk()
Window.title("Message Box")

def msgbox():
    messagebox.askokcancel("Title","Message")

Button(Window, text="MsgBox", command=msgbox).grid(row=0, column=0)
Window.mainloop()

# showinfo, showwarning, showerror, askquestion, askyesno, askokcancel


"""
the following shows how to find out what the output of clicking yes/no
in an askyesno messagebox is. This is done by storing the output into a
variable and simply printing the output, one can find out the output for
both yes and no and then do something based on the output.
"""
from tkinter import *
Window = Tk()
Window.title("Message Box")

def msgbox():
    anOutput = messagebox.askyesno("Title","Message")
    print(anOutput)

Button(Window, text="MsgBox", command=msgbox).grid(row=0, column=0)
Window.mainloop()

# showinfo, showwarning, showerror, askquestion, askyesno, askokcancel


"""
The following shows how Labels can be created based on wether a user clicked
yes or no, represented respectively by True or False.
"""
from tkinter import *
Window = Tk()
Window.title("Message Box")

def msgbox():
    anOutput = messagebox.askyesno("Title","Message")
    print(anOutput)
    if anOutput == True:
        Label(Window, text="You answered yes!").grid(row=1, column=0)
    elif anOutput == False:
        Label(Window, text="You answered no!").grid(row=1, column=0)

Button(Window, text="MsgBox", command=msgbox).grid(row=0, column=0)
Window.mainloop()

# showinfo, showwarning, showerror, askquestion, askyesno, askokcancel