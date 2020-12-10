# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 12:57:43 2020

@author: Yusef Quinlan
"""

import matplotlib.pyplot as plt

""" 
    A generic scatterplot is made with the scatter() function, note that the
    scatterplot created is created is the same way as any other plot at this
    point.
"""
x = [1,2,3,4,5,6]
y = [5,7,9,2,6,3]
plt.scatter(x,y,label="ScatterDots")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter')
plt.legend('s')

plt.show()


"""
    The following lines of code show that the marker cna be changed by using 
    the marker argument, here a star symbol has been used and the dots that 
    makr the values are now stars.
"""
plt.scatter(x,y,label="ScatterDots", marker='*')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter')
plt.legend('s')

plt.show()


"""
    Here the marker has been changed to a pentagram using p as the marker 
    argurment.
"""
plt.scatter(x,y,label="ScatterDots", marker='p')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter')
plt.legend('s')

plt.show()


"""
    The size of markers can also be changed using the s argument, I believe
    the default value is 10, it can be seen that changing the argument to 100
    vastly increases the size of the markers.
"""
plt.scatter(x,y,label="ScatterDots", marker='*', s=100)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter')
plt.legend('s')

plt.show()


"""
    The size of markers has been changed to 400 in the below code segment, and
    it can be seen that the markers are MUCH bigger than they would normally be
     as a result.
"""
plt.scatter(x,y,label="ScatterDots", marker='*', s=400)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter')
plt.legend('s')

plt.show()


"""
    colors can also be added to markers with the color argument, here a red
    has been used.
"""
plt.scatter(x,y,label="ScatterDots", marker='*', s=100, color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter')
plt.legend('s')

plt.show()