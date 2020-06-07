# -*- coding: utf-8 -*-
"""
Created on Mon May 25 18:40:09 2020

@author: Yusef Quinlan
"""
"""
The following essentially just shows how to create Radiobuttons, rather than
add functionality to them. The buttons need to use a tkinter variable, 
and the variable has been created and stored as var, and is of type tkinter int
indicated by the IntVar() function. This variable will change to the value of
any element/widget/radiobutton that is active and uses it.
"""
from tkinter import *
Window = Tk()
var = IntVar() # IntVar() is a tkinter integer
# StringVar() is a tkinger String


Label(Window, text="Pick a name").grid(row=0, column=0)
Radiobutton(Window, text="John!", variable = var, value=1).grid(row=1, column=0)
Radiobutton(Window, text="Daniel!",variable = var, value=2).grid(row=2, column=0)
Button(Window, text="Set name").grid(row=3, column=0)

Window.mainloop()



"""
In the following we add functionality to the above example, via the clickSelect()
function. Essentially we create a new label depending on the value of var,
the value of var is determined by what button is selected, if the variable of
that button is var. Both the below radio buttons use the variable var as their
variables, and they both have different values, so changing the selected button
will change the value of var. We get the value of var with the .get() function
and depending on what the value is, we make a label who's text reflects our selection
, notice that this label is made when the regular Button widget is clicked, if
a Radiobutton is selected.
"""
from tkinter import *
Window = Tk()
var = IntVar() # IntVar() is a tkinter integer
# StringVar() is a tkinger String
def clickSelect():
    text=""
    print(var.get())
    if var.get() == 1:
        text = "John was Selected!"
        Label(Window, text=text).grid(row=4,column=0)
    elif var.get() == 2:
        text = "Daniel was selected!"
        Label(Window, text=text).grid(row=4, column=0)
        


Label(Window, text="Pick a name").grid(row=0, column=0)
Radiobutton(Window, text="John!", variable = var, value=1).grid(row=1, column=0)
Radiobutton(Window, text="Daniel!",variable = var, value=2).grid(row=2, column=0)
Button(Window, text="Set name", command=clickSelect).grid(row=3, column=0)

Window.mainloop()


"""
In the following example, the variable 'var' as used by the tkinter Radiobuttons
, is set to be of value 1. This means that the John! text radiobutton will be 
the default selection when mainloop is run, as this is the only radiobutton with
a value of 1.
"""
from tkinter import *
Window = Tk()
var = IntVar() # IntVar() is a tkinter integer
# StringVar() is a tkinger String
var.set(1)
def clickSelect():
    text=""
    print(var.get())
    if var.get() == 1:
        text = "John was Selected!"
        Label(Window, text=text).grid(row=4,column=0)
    elif var.get() == 2:
        text = "Daniel was selected!"
        Label(Window, text=text).grid(row=4, column=0)
        


Label(Window, text="Pick a name").grid(row=0, column=0)
Radiobutton(Window, text="John!", variable = var, value=1).grid(row=1, column=0)
Radiobutton(Window, text="Daniel!",variable = var, value=2).grid(row=2, column=0)
Button(Window, text="Set name", command=clickSelect).grid(row=3, column=0)

Window.mainloop()



"""
The following example shows how by using different tkinter variables, Radiobuttons
can be created that can be used in seperate selections. Because the 3rd and 4th
Radiobuttons use a different variable i.e. var2, and because the clickSelect2()
function uses these variables, the second regular button creates a label based
on the second selection made, but the first two radiobuttons created have no
effect on the functionality of this second regular Button.
"""
from tkinter import *
Window = Tk()
var = IntVar() # IntVar() is a tkinter integer
# StringVar() is a tkinger String
var.set(1)
def clickSelect():
    text=""
    print(var.get())
    if var.get() == 1:
        text = "John was Selected!"
        Label(Window, text=text).grid(row=4,column=0)
    elif var.get() == 2:
        text = "Daniel was selected!"
        Label(Window, text=text).grid(row=4, column=0)
        


Label(Window, text="Pick a name").grid(row=0, column=0)
Radiobutton(Window, text="John!", variable = var, value=1).grid(row=1, column=0)
Radiobutton(Window, text="Daniel!",variable = var, value=2).grid(row=2, column=0)
Button(Window, text="Set name", command=clickSelect).grid(row=3, column=0)


var2 = StringVar()
var2.set("Anchovy")
def clickSelect2():
    text=""
    print(var2.get())
    if var2.get() == "Anchovy":
        text = "Anchovy was Selected!"
        Label(Window, text=text).grid(row=9,column=0)
    elif var2.get() == "Pinneapple":
        text = "Pinneapple was selected!"
        Label(Window, text=text).grid(row=9, column=0)
        


Label(Window, text="Pick a topping").grid(row=5, column=0)
Radiobutton(Window, text="Anchovy", variable = var2, value="Anchovy").grid(row=6, column=0)
Radiobutton(Window, text="Pinneapple",variable = var2, value="Pinneapple").grid(row=7, column=0)
Button(Window, text="Set name", command=clickSelect2).grid(row=8, column=0)
Window.mainloop()