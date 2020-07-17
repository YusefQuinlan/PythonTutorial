# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 17:59:11 2020

@author: Yusef Quinlan
"""

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
"""
 to use pyplot functions we use ply.function() such as plt.plot(arg) and 
 plt.show().
 In the following, we plot y values against an x value, the first array used
 in the plt.plot() function is the x argument and will write the horizontal
 values onto the graph/chart/whatever. The second array/argument is the y 
 argument and will write the vertical values onto the graph/chart. We can 
 think of this as plt.plot(x,y). The plt.show() function is used to show 
 plotted lines on a graph, note that plt.show() doesn't have to be used in 
 order to display the chart, but that it probably should be.
"""
plt.plot(["Monday","Tuesday","Wednesday"],[1.21,1.50,1.30])
plt.show()

# Existing arrays can be used, rather than creating arrays inside the plt.plot()
# function.
x = ["Thursday","Friday","Saturday"]
y = [4.50,5.98,4.35]

plt.plot(x,y)
plt.show()

# Here it can be seen that when two arrays of different sizes are used, that 
# an error is produced.
plt.plot([2,1],[3,4,5,6,7])
plt.show()

# Here it can be seen that two lines have been plotted onto the same graph, 
# at two distinct parts of the graph. This is due to the way that plt.show()
# works.
plt.plot(["Monday","Tuesday","Wednesday"],[1.21,1.50,1.30])
plt.plot(x,y)
plt.show()


# You can see in the next two show blocks, that plt.show() takes all the .plot()
# functions above it and puts them into the same graph.
plt.plot(["Monday","Tuesday","Wednesday"],[1.21,1.50,1.30])
plt.plot(x,y)
plt.show()

plt.plot(x,y)
plt.show()

# These two blocks are experimental blocks for fun.
plt.plot([1,1],[2,7])
plt.show()

plt.plot([1,2],[8,8])
plt.show()