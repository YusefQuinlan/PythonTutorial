# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 19:02:41 2020

@author: Yusef Quinlan
"""

import matplotlib.pyplot as plt

# making of a simple bar using the bar() function.
x = [1,3,5,7,9]
y = [8,2,4,9,6]

plt.bar(x,y, label="Barplot bar1")
plt.title("First barplot")
plt.xlabel("X label ")
plt.ylabel("Y label ")
plt.legend()
plt.show()

"""
Here the bar chart now has two distinct bars, in older versions of pyplot
these bars often render with the same colour, making one indistinguishable
from the other.
"""
x2 = [2,4,6,8,10]
y2 = [4,9,2,5,7]

plt.bar(x,y, label="Barplot bar1")
plt.bar(x2,y2, label="Barplot bar2")
plt.title("First barplot")
plt.xlabel("X label ")
plt.ylabel("Y label ")
plt.legend()
plt.show()

"""
Below the bars colours have been changed, you may want to change default
colours so that your plots convey a certain style.
"""
plt.bar(x,y, label="Barplot bar1", color="pink")
plt.bar(x2,y2, label="Barplot bar2", color="yellow")
plt.title("First barplot")
plt.xlabel("X label ")
plt.ylabel("Y label ")
plt.legend()
plt.show()

"""
The following is the use of a histogram, histograms actually show the amount of
times a value in a certain range shows up, for example how often an iq value
in the range 70-80 shows up or 100-110, bins control the ranges of histograms.
"""
iqs = [55,100,89,75,125,180,95,67,82,99,107,76,120,67,89,91,109,78,67,90,100,105]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180]
plt.hist(iqs,bins,histtype='bar',width=0.75,label="iqs")
plt.title("First barplot")
plt.xlabel("X label ")
plt.ylabel("Y label ")
plt.legend()
plt.show()


"""
Below I have deleted some of the bins to show that the chart has become more
accurate, however the max width limits the size of the bin lines
"""
iqs = [55,100,89,75,125,180,95,67,82,99,107,76,120,67,89,91,109,78,67,90,100,105]
bins = [50,60,70,80,90,100,120,130,180]
plt.hist(iqs,bins,histtype='bar',width=0.75,label="iqs")
plt.title("First barplot")
plt.xlabel("X label ")
plt.ylabel("Y label ")
plt.legend()
plt.show()

"""
Below it can be seen that getting rid of the width entirely, causes another 
problem. Now items in different ranges overflow from bin to bin, and it is hard
to tell how many items are in each range and where a range starts or ends.
"""
iqs = [55,100,89,75,125,180,95,67,82,99,107,76,120,67,89,91,109,78,67,90,100,105]
bins = [50,60,70,80,90,100,120,130,180]
plt.hist(iqs,bins,histtype='bar',label="iqs")
plt.title("First barplot")
plt.xlabel("X label ")
plt.ylabel("Y label ")
plt.legend()
plt.show()

# Below width is better
iqs = [55,100,89,75,125,180,95,67,82,99,107,76,120,67,89,91,109,78,67,90,100,105]
bins = [50,60,70,80,90,100,120,130,180]
plt.hist(iqs,bins,histtype='bar',width=2,label="iqs")
plt.title("First barplot")
plt.xlabel("X label ")
plt.ylabel("Y label ")
plt.legend()
plt.show()

# Again more improvement
iqs = [55,100,89,75,125,180,95,67,82,99,107,76,120,67,89,91,109,78,67,90,100,105]
bins = [50,60,70,80,90,100,120,130,180]
plt.hist(iqs,bins,histtype='bar',width=5,label="iqs")
plt.title("First barplot")
plt.xlabel("X label ")
plt.ylabel("Y label ")
plt.legend()
plt.show()

"""
And now I run into problems again, you can fiddle with the bins and widths as
please. And different adjustment will have different effects on the chart 
layout.
"""
iqs = [55,100,89,75,125,180,95,67,82,99,107,76,120,67,89,91,109,78,67,90,100,105]
bins = [50,60,70,80,90,100,120,130]
plt.hist(iqs,bins,histtype='bar',width=7,label="iqs")
plt.title("First barplot")
plt.xlabel("X label ")
plt.ylabel("Y label ")
plt.legend()
plt.show()