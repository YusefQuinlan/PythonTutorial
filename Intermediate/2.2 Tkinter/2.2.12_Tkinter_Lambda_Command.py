# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 18:10:54 2020

@author: Yusef Quinlan
"""


"""
 The following demonstrates that using the button without passing an argument
 to the function xreturn() an error is produced.
 """
from tkinter import *
Window =Tk()
Window.title("Lambdas")
Label1 = Label(Window,text="The following button returns x times 8")
Label1.pack()
x = 3
def xreturn(j):
    Label(Window, text=str(x * j)).pack()
Button1 = Button(Window, text="this button returns x times 8", command=xreturn).pack()
Window.mainloop()

"""
if we pass 8 to the xreturn command normally then the xreturn function packs a
label of the value x * 8 before the button renders and the button does not function
as intended, no idea why this happens in tkinter, but for whatever reason one
cannot simply pass a function with an argument to the command parameter of a
tkinter widget.
"""
from tkinter import *
Window =Tk()
Window.title("Lambdas")
Label1 = Label(Window,text="The following button returns x times 8")
Label1.pack()
x = 3
def xreturn(j):
    Label(Window, text=str(x * j)).pack()
Button1 = Button(Window, text="this button returns x times 8", command=xreturn(8)).pack()
Window.mainloop()

"""
 However by passing the command as a lambda and passing a value into a variable and
 using the function with that variable as an argument, we can use the function
 with a parameter without any weird errors or unintended functionality.
"""
from tkinter import *
Window =Tk()
Window.title("Lambdas")
Label1 = Label(Window,text="The following button returns x times 8")
Label1.pack()
x = 3
def xreturn(j):
    Label(Window, text=str(x * j)).pack()
Button1 = Button(Window, text="this button returns x times 8", command= lambda j=8: xreturn(j)).pack()
Window.mainloop()


 """
 The following demonstrates that we can pass several argument values to 
 xreturn(j) to several buttons, and they all work as intended thanks to lambda.
 """
from tkinter import *
Window =Tk()
Window.title("Lambdas")
Label1 = Label(Window,text="The following button returns x times 8")
Label1.pack()
x = 3
def xreturn(j):
    Label(Window, text=str(x * j)).pack()
Button1 = Button(Window, text="this button returns x times 8", command= lambda j=8: xreturn(j)).pack()
Button2 = Button(Window, text="this button returns x times 5", command= lambda j=5: xreturn(j)).pack()
Button3 = Button(Window, text="this button returns x times 2", command= lambda j=2: xreturn(j)).pack()
Window.mainloop()

# Showing that lambda can be used for more than one function such as xset.
from tkinter import *
Window =Tk()
Window.title("Lambdas")
Label1 = Label(Window,text="The following button returns x times 8")
Label1.pack()
x = 3
def xreturn(j):
    Label(Window, text=str(x * j)).pack()
def xset(i):
    global x
    x = i
Button1 = Button(Window, text="this button returns x times 8", command= lambda j=8: xreturn(j)).pack()
Button2 = Button(Window, text="this button returns x times 5", command= lambda j=5: xreturn(j)).pack()
Button3 = Button(Window, text="this button returns x times 2", command= lambda j=2: xreturn(j)).pack()
Button4 = Button(Window, text="this button sets x to 2", command= lambda setval=2: xset(setval)).pack()

Window.mainloop()