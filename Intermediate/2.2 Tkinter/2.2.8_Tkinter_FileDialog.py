# -*- coding: utf-8 -*-
"""
Created on Tue May 26 17:52:07 2020

@author: Yusef Quinlan
"""
"""
the filedialog.askopenfilename allows for us to open files of specified types.
It asks us for our intial directory i.e. where we want to start looking for
files. It asks for a title, the title of the file opener Window, and it asks 
what filetypes we want to search for. To select our filetypes we give either a
name or a * symbol, followed by a dot (.) and then the file extension or a *
symbol. The * symbol represents all, the first symbol is the filename and the
second the file extension, the following would search for all jpg files with
'Jason' in their name :    ("Jason.jpg"), the following searches for any name
and any file:   ("*.*"),   the following searches for a specific name (DAN)
 but any  filetype:     ("DAN.*"), the final example searches or allows us to
 find any filename but only of the .wav extension:   ("*.wav").
The filedialog only returns the file-location and if nothing is done with that
location, then the function does nothing in practice other than return. 
"""
from tkinter import *
from tkinter import filedialog
Window=Tk()
Window.title("MainWindow")

fileloc = filedialog.askopenfilename(initialdir="/", title="Select a file",
                                     filetypes=(("all files","*.*"),("jpg files","*.jpg")))

Window.mainloop()


"""
Here by printing the fileloc variable we can see the location of our selected
file, printed out in terminal.
"""
from tkinter import *
from tkinter import filedialog
Window=Tk()
Window.title("MainWindow")

fileloc = filedialog.askopenfilename(initialdir="/", title="Select a file",
                                     filetypes=(("all files","*.*"),("jpg files","*.jpg")))
print(fileloc)

Window.mainloop()



# and now instead of allowing the filedialog to open by default, the button
# opens the filedialog to get a files exact location.
from tkinter import *
from tkinter import filedialog
Window=Tk()
Window.title("MainWindow")

def filelocater():
    fileloc = filedialog.askopenfilename(initialdir="/", title="Select a file",
                                     filetypes=(("all files","*.*"),("jpg files","*.jpg")))
    print(fileloc)

Button(Window, text="Get a file location", command=filelocater).pack()
Window.mainloop()