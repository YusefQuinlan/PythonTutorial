# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 19:28:46 2020

@author: Yusef Quinlan
"""
# Initial creation of a Notebook with two tabs in it
from tkinter import *
from tkinter import ttk
import webbrowser
Window=Tk()
Window.title("Open Html")
aNotebook = ttk.Notebook(Window)
aNotebook.pack()
aFrame = Frame(aNotebook)
aFrame2 = Frame(aNotebook)
aFrame.pack(fill="both",expand=1)
aFrame2.pack(fill="both",expand=1)
aNotebook.add(aFrame, text="first html")
aNotebook.add(aFrame2, text="second html")
Window.mainloop()

""" to the first tab in the Notebook, a buch of buttons are added, the buttons
    have text that corresponds to a url from a url list, when clicked, these
    button will open the ul in a users browser. Demonstrating that a user
    can make an interface to open websites using tkinter.
"""
from tkinter import *
from tkinter import ttk
import webbrowser
Window=Tk()
Window.title("Open Html")
aNotebook = ttk.Notebook(Window)
aNotebook.pack()
aFrame = Frame(aNotebook)
aFrame2 = Frame(aNotebook)
aFrame.pack(fill="both",expand=1)
aFrame2.pack(fill="both",expand=1)
aNotebook.add(aFrame, text="first html")
aNotebook.add(aFrame2, text="second html")
urls = ["https://www.google.com/","https://www.youtube.com/", "https://www.facebook.com/","https://espanol.yahoo.com/?p=us",
"https://en.wikipedia.org/wiki/Wikipedia"]
urls2 = ["deded","preoe","erterte"]
def openSite(url):
    webbrowser.open(url, new=2)
for i in urls:
    Button(aFrame, text=i, command= lambda x=i: openSite(x)).pack()  
Window.mainloop()

"""
    A second set of buttons corresponding to a second url list are added to the
    second tab, they are dummy urls and not real websites, so when opened they
    don't connect to a webpage. But this shows how easily one could make an
    interface in tkinter, that could take lists of urls and make buttons
    to open them, in several tabs. Each tab could have its own genre, and as
    long as one had an url list for each genere, it would be rather easy to do.
    Obviously, a scrollbar would be needed to scroll through urls if the lists
    are large enough, and title might need to be made dynamically if there are
    many tabs, but it is achievable, with tkinter.
"""
from tkinter import *
from tkinter import ttk
import webbrowser
Window=Tk()
Window.title("Open Html")
aNotebook = ttk.Notebook(Window)
aNotebook.pack()
aFrame = Frame(aNotebook)
aFrame2 = Frame(aNotebook)
aFrame.pack(fill="both",expand=1)
aFrame2.pack(fill="both",expand=1)
aNotebook.add(aFrame, text="first html")
aNotebook.add(aFrame2, text="second html")
urls = ["https://www.google.com/","https://www.youtube.com/", "https://www.facebook.com/","https://espanol.yahoo.com/?p=us",
"https://en.wikipedia.org/wiki/Wikipedia"]
urls2 = ["deded","preoe","erterte"]
def openSite(url):
    webbrowser.open(url, new=2)
for i in urls:
    Button(aFrame, text=i, command= lambda x=i: openSite(x)).pack()
for i in urls2:
    Button(aFrame2, text=i, command= lambda x=i: openSite(x)).pack()   
Window.mainloop()