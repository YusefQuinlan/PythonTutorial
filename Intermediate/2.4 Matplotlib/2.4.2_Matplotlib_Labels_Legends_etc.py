# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 16:17:50 2020

@author: Yusef Quinlan
"""
# import pyplot
import matplotlib.pyplot as plt

"""
 Here we make a regular chart it has not title and the x and y labels
 are not clearly labelled, in addition there are numbers in between the
 1,2 and 3 values on the xlabel and numbers in between the 2,4 and 6 values
 on the ylabel, this may be seen as undesirable
"""

x = [1,2,3]
y = [2,4,6]

plt.plot(x,y)
plt.show()

"""
In the following chart, a title is added to the chart with the title(titlename)
function, and the x and y labels are added using the xlabel(labelname) and the
ylabel(labelname) function respectively. This helps users clarify what the 
chart might represent, for now I have added generic names, try changing them
and experimenting in your own time.
"""
x = [1,2,3]
y = [2,4,6]

plt.plot(x,y)
plt.title("Y = 2 times X")
plt.xlabel("X label")
plt.ylabel("Y label")
plt.show()


"""
Here in addition to adding a title and x/y labels, I have changed the font type
of the title to Times New Roman using a fontdict and increased the titles
fontsize using the same fontdict. I have also changed the x and y ticks using 
the xticks(ticks) and yticks(ticks) functions respectively. Now there are no
'ticks' in between the x and the y array numbers.
"""
plt.plot(x,y)
plt.title("Y = 2 times X", fontdict={'fontname':'Times New Roman','fontsize':30})
plt.xlabel("X label")
plt.ylabel("Y label")
plt.xticks(x)
plt.yticks([2,4,6])
plt.show()

"""
The following code shows what happens when The tick maximum of the x or y
axis is far larger than the second to last value, basically pyplot resizes the
chart/graph to the size of the range between the minimum and maximum tick 
values. Resizes in such cases can be undesirable. 
""" 
plt.plot(x,y)
plt.title("Y = 2 times X", fontdict={'fontname':'Times New Roman','fontsize':30})
plt.xlabel("X label")
plt.ylabel("Y label")
plt.xticks([1,2,80])
plt.yticks([2,4,6])
plt.show()


"""
The following block of code shows how adding a label to a plot and a legend
for the labels adds a legend that can inform users what a line represents.
This is done by adding a label as a plot(x,y,label) argument and using the
legend() function. It is intended to be used to help users distinguish between
Multiple lines.
"""
plt.plot(x,y,label="A line")
plt.title("Y = 2 times X", fontdict={'fontname':'Times New Roman','fontsize':30})
plt.xlabel("X label")
plt.ylabel("Y label")
plt.xticks(x)
plt.yticks([2,4,6])
plt.legend()
plt.show()


"""
The code below just shows how legends can be used to distinguish between 
several lines, notice that the legend is the box that holds the labels for the 
different plots, and each plot is its own line.
"""

plt.plot(x,y,label="Line 1")
plt.plot([1.5,2.5,4],y,label="Line 2")
plt.title("Y = 2 times X", fontdict={'fontname':'Times New Roman','fontsize':30})
plt.xlabel("X label")
plt.ylabel("Y label")
plt.xticks(x)
plt.yticks([2,4,6])
plt.legend()
plt.show()


# Here I have added names to the labels to show how labels might be applied.
plt.plot(x,y,label="Cabbages")
plt.plot([1.5,2.5,4],y,label="Bananas")
plt.title("Y = 2 times X", fontdict={'fontname':'Times New Roman','fontsize':30})
plt.xlabel("X label")
plt.ylabel("Y label")
plt.xticks(x)
plt.yticks([2,4,6])
plt.legend()
plt.show()


"""
If you add labels but no legend, You won't see your labels as they have no 
legend that they can be assigned to.
"""
plt.plot(x,y,label="Cabbages")
plt.plot([1.5,2.5,4],y,label="Bananas")
plt.title("Y = 2 times X", fontdict={'fontname':'Times New Roman','fontsize':30})
plt.xlabel("X label")
plt.ylabel("Y label")
plt.xticks(x)
plt.yticks([2,4,6])
plt.show()


"""
If you add legends with no labels, you will usually actually still get a legend 
appear in some spot on your chart/graph, but it will just be an empty box as it
has no labels to hold inside of it.
"""
plt.plot(x,y)
plt.plot([1.5,2.5,4],y)
plt.title("Y = 2 times X", fontdict={'fontname':'Times New Roman','fontsize':30})
plt.xlabel("X label")
plt.ylabel("Y label")
plt.xticks(x)
plt.yticks([2,4,6])
plt.legend()
plt.show()