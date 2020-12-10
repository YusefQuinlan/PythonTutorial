# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 14:58:11 2020

@author: Yusef Quinlan
"""
"""
Pie charts are circular charts that give a visual representation that
shows what proportion of a set of a figures certain items take up. They use 
slices to represent items like slices of a pie. So for example if we had the
following items : item1, item2 and item3 with the corresponding values [1,2,3]
then item 1 would take up 1/6 of the pie chart as the sum of the values is six 
and 1 divided by six is 1/6. item2 would take up 2/6 of the chart and would be
twice as large as item1, and item3 would take up 3/6 or 1/2 of the chart and 
would be 3 times larger than item1. Practical examples and explanations for
such examples can be seen below.
"""

import matplotlib.pyplot as plt

"""
Here a pie chart is made with the following slice values [9,12,33,12,17],
and the following items have those slice values : ["Asians", "Africans",
"Caucasoid", "Latinos", "Aborigines"]. So for example the item "Asians" has
the value 9 and the item Latinos "has" the value 12. 
plt.pie() function creates a pie chart and we must put in our slice values and 
labels for those values as arguments, in this case we have used the variable
'slices' as our slice values argument and the variable items as our labels 
argument. And this produces a pie chart with default colours. Note there is
no title and our slices/labels arguments should be lists (and possibly arrays).
"""
slices = [9,12,33,12,17]
items = ["Asians","Africans","Caucasoid","Latinos","Aborigines"]

plt.pie(slices,labels=items)
plt.show()

# The following chart is the same as the above chart only it also includes a 
# title.
plt.pie(slices,labels=items)
plt.title("Proportion of races affected by xex disease")
plt.show()

"""
    This chart is almost the same as the one above it, the only difference 
    being that custom colours have been chosen for it via the colors argument.
    Note that the colors argument takes a list of values 
    (and possibly an array of values).
"""
plt.pie(slices,labels=items,colors=['pink','blue','orange','yellow','grey'])
plt.title("Proportion of races affected by xex disease")
plt.show()

"""
    Here the colors argument uses a premade array and startangle has been added
    essentially this has changed the angle at which the pie chart labels start
    displaying, I have chosen to change this by 90 degrees, and if you look at
    this chart and compare it to the previous one, you can see that the first
    label ("Asians") starts 90 degrees left of where it started before.
"""
colorpea = ['pink','blue','orange','yellow','grey']
plt.pie(slices,labels=items,colors=colorpea,startangle = 90)
plt.title("Proportion of races affected by xex disease")
plt.show()

# The only change here is the addition of a shadow, that can be seen below the
# Caucasoid slice.
plt.pie(slices,labels=items,colors=colorpea,startangle=90,shadow=True)
plt.title("Proportion of races affected by xex disease")
plt.show()

"""
    Here the startangle and shadow argument have been removed and the explode
    function has been added. Exploded items/labels basically come out of the 
    pie chart to sort of demonstrate where they are, this may be used because
    some labels may be more important to highlight than others, any argument 
    above 0 will explode an item, and items are exploded in order of labels,
    so for example index [0] of your label/slices lists/arrays will be index[0]
    of your explode argument parameters. In this case both index [2] and [4] 
    i.e. "Caucasoid" and "Aborigines" have been exploded.
"""
plt.pie(slices,labels=items, explode=(0,0,0.3,0,0.1),colors=colorpea)
plt.title("Proportion of races affected by xex disease")
plt.show()

# Here only "Caucasoid" has been exploded.
plt.pie(slices,labels=items, explode=(0,0,0.2,0,0),colors=colorpea)
plt.title("Proportion of races affected by xex disease")
plt.show()

# the autopct argument shows what percentage of the sum of slice values
# each slice takes up.
plt.pie(slices,labels=items, autopct='%1.1f%%',colors=colorpea)
plt.title("Proportion of races affected by xex disease")
plt.show()