# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 16:10:57 2020

@author: Yusef Quinlan
"""
from tkinter import *
from tkinter import ttk
#Regular window with notebook inside of it, note that the notebook displays as
# an almost unseen square that is black. This is because the frames have been 
# added to it, and it has been added to the window, but without the use of
# Notebook.add(frame/element), the tabs aren't rendered properly.
Window = Tk()
Window.title("Notebook")
aNotebook = ttk.Notebook(Window)
aNotebook.pack(pady=20)
aFrame = Frame(aNotebook, bg = "black")
aFrame2 = Frame(aNotebook, bg="yellow")
aFrame.pack(fill="both", expand=1)
aFrame2.pack(fill="both",expand=1)

Window.mainloop()

# You can see that the .add() functions make the tabs render correctly.
from tkinter import *
from tkinter import ttk

Window = Tk()
Window.title("Notebook")
aNotebook = ttk.Notebook(Window)
aNotebook.pack(pady=20)
aFrame = Frame(aNotebook, bg = "black")
aFrame2 = Frame(aNotebook, bg="yellow")
aFrame.pack(fill="both", expand=1)
aFrame2.pack(fill="both",expand=1)
aNotebook.add(aFrame, text="first frame")
aNotebook.add(aFrame2, text="second frame")

Window.mainloop()

# Adding width and height allows us to have more full frames.
from tkinter import *
from tkinter import ttk

Window = Tk()
Window.title("Notebook")
aNotebook = ttk.Notebook(Window)
aNotebook.pack(pady=20)
aFrame = Frame(aNotebook, bg = "black", width=250, height=250)
aFrame2 = Frame(aNotebook, bg="yellow", width=250, height=250)
aFrame.pack(fill="both", expand=1)
aFrame2.pack(fill="both",expand=1)
aNotebook.add(aFrame, text="first frame")
aNotebook.add(aFrame2, text="second frame")

Window.mainloop()

# An example of hiding and navigating tabs.
from tkinter import *
from tkinter import ttk

Window = Tk()
Window.title("Notebook")
aNotebook = ttk.Notebook(Window)
aNotebook.pack(pady=20)
aFrame = Frame(aNotebook, bg = "blue", width=250, height=250)
aFrame2 = Frame(aNotebook, bg="yellow", width=250, height=250)
aFrame.pack(fill="both", expand=1)
aFrame2.pack(fill="both",expand=1)
aNotebook.add(aFrame, text="first frame")
aNotebook.add(aFrame2, text="second frame")

def invis():
    aNotebook.hide(1)
def nav():
    aNotebook.select(1)
Button(aFrame, text="hide frame number 2", command=invis).pack()
Button(aFrame, text="navigate to Frame 2", command=nav).pack()
Window.mainloop()