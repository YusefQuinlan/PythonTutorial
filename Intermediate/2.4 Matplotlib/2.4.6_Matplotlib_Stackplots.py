# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 15:03:14 2020

@author: Yusef Quinlan
"""

import matplotlib.pyplot as plt


"""
    The creation of a stackplot with the use of the stackplot() function, as 
    can be seen the stackplot takes an x argument and then several y arguments
    rather than a single y argument. The y values for each x coordinate are 
    summed up, and the y stacks are stacked against eachother so that the 
    proportion that a particular set of y values takes up in comparison to 
    other y values can be seen.
"""
x = [1,2,3,4,5]
y1 = [1,1,2,3,1]
y2 = [6,2,4,1,1]
y3 = [3,7,4,6,8]
plt.stackplot(x,y1,y2,y3)
plt.xlabel('x')
plt.ylabel('y')
plt.show()


"""
    Below we can see that by adding the colors argument, we can change the
    colours used by our stackplot.
"""

plt.stackplot(x,y1,y2,y3,colors=['r','blue','pink'])
plt.xlabel('x')
plt.ylabel('y')
plt.show()

"""
    Now with the addition of the labels argument, we can now label our various
    stacks in order to determine what they relate to.
"""
plt.stackplot(x,y1,y2,y3,labels=['y1','y2','y3'],colors=['r','blue','pink'])
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


"""
    Showing a real example.
"""
Sales_years = [2001,2002,2003,2004,2005]
Mammals = [4000,3700,3000,2000,1000]
Reptiles = [2500,3000,4000,5000,6000]
Fish = [3500,3300,3000,3000,3000]

plt.stackplot(Sales_years,Mammals,Reptiles,Fish, labels=['Mammal','Reptile','Fish'])
plt.xlabel('Year')
plt.ylabel('Amount_Sold')
plt.legend()
plt.title('Pets sold per year')
plt.show()