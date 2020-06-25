# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 16:09:39 2020

@author: Yusef Quinlan
"""

#First set of code showing creation of a Listbox
from tkinter import*
Window= Tk()
Window.title("Listboxes")
aListbox = Listbox(Window)
aListbox.grid(row=0,column=0, pady=15)
Window.mainloop()

"""
 The following shows how to insert a value into a listbox, remember that 
 listbox values must be strings. And the listbox.insert() function takes
 to arguments, the first is the index you want to insert the item to,
 the second is the item itself.
 """
from tkinter import*
Window= Tk()
Window.title("Listboxes")
aListbox = Listbox(Window)
aListbox.grid(row=0,column=0, pady=15)
aListbox.insert(0,"1")
Window.mainloop()

# The following shows multiple insertion and the consequence of inserting items
# at index '0'
from tkinter import*
Window= Tk()
Window.title("Listboxes")
aListbox = Listbox(Window)
aListbox.grid(row=0,column=0, pady=15)
aListbox.insert(0,"1")
aListbox.insert(0, "2")
aListbox.insert(0, "3")
Window.mainloop()

# The following shows how to insert items at the end of the list with the END
# keyword as an index argument.
from tkinter import*
Window= Tk()
Window.title("Listboxes")
aListbox = Listbox(Window)
aListbox.grid(row=0,column=0, pady=15)
aListbox.insert(END,"1")
aListbox.insert(END, "2")
aListbox.insert(END, "3")
Window.mainloop()

# The following shows deletion with the listbox.delete() function, the ANCHOR
# value is the value of the currently selected item. 
from tkinter import*
Window= Tk()
Window.title("Listboxes")
aListbox = Listbox(Window)
aListbox.grid(row=0,column=0, pady=15)
aListbox.insert(END,"1")
aListbox.insert(END, "2")
aListbox.insert(END, "3")
def remove():
    aListbox.delete(ANCHOR)
aButton = Button(Window, text="remove current item", command=remove)
aButton.grid(row=1,column=0)
Window.mainloop()


# Listbox.curselection() can be used in place of ANCHOR
from tkinter import*
Window= Tk()
Window.title("Listboxes")
aListbox = Listbox(Window)
aListbox.grid(row=0,column=0, pady=15)
aListbox.insert(END,"1")
aListbox.insert(END, "2")
aListbox.insert(END, "3")
def remove():
    aListbox.delete(aListbox.curselection())
aButton = Button(Window, text="remove current item", command=remove)
aButton.grid(row=1,column=0)
Window.mainloop()

# One can get items using Listbox.get(ANCHOR).
from tkinter import*
Window= Tk()
Window.title("Listboxes")
aListbox = Listbox(Window)
aListbox.grid(row=0,column=0, pady=15)
aListbox.insert(END,"1")
aListbox.insert(END, "2")
aListbox.insert(END, "3")
def remove():
    aListbox.delete(aListbox.curselection())
def getitem():
    value = aListbox.get(ANCHOR)
    print(value)
aButton = Button(Window, text="remove current item", command=remove)
aButton.grid(row=1,column=0)
aButton2 = Button(Window, text="get current item", command=getitem)
aButton2.grid(row=2, column=0)

Window.mainloop()

# The following shows how to add all items of a list to a listbox with a for loop.
from tkinter import*
Window= Tk()
Window.title("Listboxes")
aListbox = Listbox(Window)
aListbox.grid(row=0,column=0, pady=15)
alist = ["1","2","3","4","5"]
for i in alist:
    aListbox.insert(END, i)
def remove():
    aListbox.delete(aListbox.curselection())
def getitem():
    value = aListbox.get(ANCHOR)
    print(value)
aButton = Button(Window, text="remove current item", command=remove)
aButton.grid(row=1,column=0)
aButton2 = Button(Window, text="get current item", command=getitem)
aButton2.grid(row=2, column=0)

Window.mainloop()

"""
 When you open this window, you will see that there is no scrollbar, whilst a
 user can scroll without one, not all users will know they can scroll through 
 the listbox without a scrollbar so it is best to add one.
"""
from tkinter import*
Window= Tk()
Window.title("Listboxes")
aListbox = Listbox(Window)
aListbox.grid(row=0,column=0, pady=15)
for i in range(10):
    aListbox.insert(END, "Hello")
    aListbox.insert(END, "goodbye")
    aListbox.insert(END, "aval")
aListbox.insert(END,"END")
def remove():
    aListbox.delete(aListbox.curselection())
def getitem():
    value = aListbox.get(ANCHOR)
    print(value)
aButton = Button(Window, text="remove current item", command=remove)
aButton.grid(row=1,column=0)
aButton2 = Button(Window, text="get current item", command=getitem)
aButton2.grid(row=2, column=0)

Window.mainloop()

"""
One can add a scrollbar to a window, but they must bind it to the listbox in 
order for it to have an effect on the listbox when used, below a scrollbar was
added to a window but not binded/connected to the Listbox.
"""
from tkinter import*
Window= Tk()
Window.title("Listboxes")
scroll = Scrollbar(Window)
aListbox = Listbox(Window)
scroll.grid(row=0, column=1)
aListbox.grid(row=0,column=0, pady=15)
for i in range(10):
    aListbox.insert(END, "Hello")
    aListbox.insert(END, "goodbye")
    aListbox.insert(END, "aval")
aListbox.insert(END,"END")
def remove():
    aListbox.delete(aListbox.curselection())
def getitem():
    value = aListbox.get(ANCHOR)
    print(value)
aButton = Button(Window, text="remove current item", command=remove)
aButton.grid(row=1,column=0)
aButton2 = Button(Window, text="get current item", command=getitem)
aButton2.grid(row=2, column=0)

Window.mainloop()

"""
Below you can see that the scrollbar has been binded/connected to the listbox 
via the scroll['command'] = aListbox.yview and the 
aListbox['yscrollcommand'] = scoll.set lines of code. But the scrollbar is too
small to register scroll changes, so whilst you can use the scroolbar to scroll
through the Listbox, you can't see how far up or down the listbox you are.
"""
from tkinter import*
Window= Tk()
Window.title("Listboxes")
scroll = Scrollbar(Window)
aListbox = Listbox(Window)
scroll.grid(row=0, column=1)
aListbox.grid(row=0,column=0, pady=15)
scroll['command'] = aListbox.yview
aListbox['yscrollcommand'] = scroll.set
for i in range(10):
    aListbox.insert(END, "Hello")
    aListbox.insert(END, "goodbye")
    aListbox.insert(END, "aval")
aListbox.insert(END,"END")
def remove():
    aListbox.delete(aListbox.curselection())
def getitem():
    value = aListbox.get(ANCHOR)
    print(value)
aButton = Button(Window, text="remove current item", command=remove)
aButton.grid(row=1,column=0)
aButton2 = Button(Window, text="get current item", command=getitem)
aButton2.grid(row=2, column=0)

Window.mainloop()

# with the addition of sticky='ns' to the .grid() function, the scrollbar now
# works as intended.
from tkinter import*
Window= Tk()
Window.title("Listboxes")
scroll = Scrollbar(Window)
aListbox = Listbox(Window)
scroll.grid(row=0, column=1, sticky='ns')
aListbox.grid(row=0,column=0, pady=15)
scroll['command'] = aListbox.yview
aListbox['yscrollcommand'] = scroll.set
for i in range(10):
    aListbox.insert(END, "Hello")
    aListbox.insert(END, "goodbye")
    aListbox.insert(END, "aval")
aListbox.insert(END,"END")
def remove():
    aListbox.delete(aListbox.curselection())
def getitem():
    value = aListbox.get(ANCHOR)
    print(value)
aButton = Button(Window, text="remove current item", command=remove)
aButton.grid(row=1,column=0)
aButton2 = Button(Window, text="get current item", command=getitem)
aButton2.grid(row=2, column=0)

Window.mainloop()