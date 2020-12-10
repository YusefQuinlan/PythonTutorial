# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 14:30:24 2020

@author: Yusef Quinlan
"""
# Making a normal plot
import matplotlib.pyplot as plt
x = [1,2,3]
y = [5,10,20]
plt.plot(x,y)
plt.show()


"""
Here a figuresize is declared before a plot is created via the figure() function
the figsize argument of the function, requires two comma seperated values 
inside curly braces (parenthesis). The first of these values is the x value
and the second is the y value. The larger the x value, the wider the plot
will be, and the larger the y value the taller the plot will be. So basically
the figsize argument allows changing of the x:y ratio.
"""
plt.figure(figsize=(10,3))
plt.plot(x,y)
plt.show()

""" 
If the figure function is used below your plot function, then there is a chance
that your plot figure size will not change.
"""
plt.plot(x,y)
plt.figure(figsize=(10,3))
plt.show()


# Demonstrates that a larger x figsize value produces a long and short plot.
plt.figure(figsize=(15,3))
plt.bar(x,y)
plt.show()

"""
 Here the plot is as tall as it is high, note that any plot type can be changed
 Here a bar has been created rather than a regular graph.
"""
plt.figure(figsize=(10,10))
plt.bar(x,y)
plt.show()

"""
the dpi argument of the figure() function, can alter the pixel density per
inch. The higher the dpi value, the larger the chart will be, and the lower it
is, the smaller it will be, smaller dpi values will lead to lower resolution
plots. The default dpi value is 72.
"""
plt.figure(figsize=(10,10), dpi=72)
plt.bar(x,y)
plt.show()


# This 20 dpi plot shows that lower dpi value equates to lower image quality
plt.figure(figsize=(10,10), dpi=20)
plt.bar(x,y)
plt.show()

# A larger plot is produced because the dpi value is high.
plt.figure(figsize=(10,10), dpi=300)
plt.bar(x,y)
plt.show()

"""
Here a barchart is saved to the directory the code is run in, via use of the
savefig() function. Any type of plot can be saved using the savefig() 
function, and the desired filename can be selected by adding a name as a string
value. Note that if you name a plot after an existing image file in the same
directory, you may unintentionally end up overwriting the existing file. 
"""
plt.figure(figsize=(10,10))
plt.bar(x,y)
plt.savefig("A barchart")
plt.show()

# Savefig() can also take a dpi value as an argument.
plt.figure(figsize=(10,10))
plt.bar(x,y)
plt.savefig("A barchart 2", dpi=20)
plt.show()

"""
By adding the .jpg extension to the title-string, files can be saved as jpg
files, rather than as pdf files.
"""

plt.figure(figsize=(10,10))
plt.bar(x,y)
plt.savefig("A bsed.jpg", dpi=20)
plt.show()