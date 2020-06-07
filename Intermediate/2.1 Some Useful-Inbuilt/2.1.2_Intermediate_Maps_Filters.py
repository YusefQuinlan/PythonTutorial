# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 12:31:52 2019

@author: Yusef Quinlan
"""
#A map is a way of using a function on every item in an array.

""""
A function is defined and the function is applied to every number in a list
the numbers the function is applied to are appended to another list, this takes 6
lines of code other than the first list declaration.
""""
def squared(x):
    return x * x

Numbers = [6,6,5,7,8,2,6,3]

Numbers2 = []
for num in Numbers:
    aNum = squared(num)
    Numbers2.append(aNum)
  
#Printing the results
print(Numbers2)

#A map function being defined with the form: map(function, list)   
# The function returns a map object and is not useful to us at present
map(squared, Numbers)

#The map object is converted into a list that is the same as 'Numbers2'
# Note that using this map function and the for declaration only takes 3 lines
# of code.
list(map(squared, Numbers))

#The map object is converted and then a lambda is used instead of a predefined
# Function, this take sonly one line of code to write.
list(map(lambda x: x*x, Numbers))

#Map objects can work over other iterable objects as in the following example
#with a dictionary.
Dict1 = {"er":22,"l":9}
list(map(lambda x: x, Dict1))

"""
A filter function can be used to filter out items in a list, here we use the
keyword filter and as an argument a function or the word 'None' followed
by an iterable object to filter i.e. an array. In this particular filter
the lambda filters out all objects that are not greater than 5.
"""
list(filter(lambda x: x > 5, Numbers))


#In the following filtration the 'None' argument is used, this signals that we want
# to return all values that are not 'None'
Namelist = ["Kavinder", "Malaga", "", "", "Tiffany", "Jeremy", ""]
list(filter(None, NameList))

#None refers to the following: None, 0, "", 0.0, 0j, [], (), {}, False

L = None
print(L)

#Filtering out 'None' values once again.
MixList = [3,7,"",0,22,[],[],"Hello"]
list(filter(None, MixList))