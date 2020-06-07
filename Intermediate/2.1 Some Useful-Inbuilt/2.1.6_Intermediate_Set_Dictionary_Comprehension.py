# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 15:37:15 2019

@author: Yusef Quinlan
"""
#In the following its actually less effort to use a set(list) conversion
# rather than use set comprehension to convert the list.
l1 = [5,6,7,8,8,9,5]
set(x for x in l1)
set(l1)

#Making a list with a set comprehension and converting it to a set with set(list)
l2 = [x**2 for x in range(-3,4)]
l2
set(l2)

#If the list is not needed then its easier and faster to use a set comprehension
# in this case.
set(x**2 for x in range(-3,4))

#Zipping two arrays together so that they can be used together to create dictionaries
# lists of tuples or perhaps used with complex functions.
z1 = zip(l1,l2)
z1

#Printing a list of the zip returns a list of tuples based on the zipped lists.
print(list(z1))

l3 = [1,2,3]
l4 = [1,2,3,4,5]

"""
 When printing a list of a zip of two lists of different lengths, it can be seen
 that the zip only zips two lists together up to the last iteration of the shortest
 list/array. In this example the first array contains 3 iterables/items and 
 the second array contains 5 iterables/items, note that the zip only produces
 three tuples in the tuple list....
"""

print(list(zip(l3,l4)))

"""
 Dictionaries can be made from zips by using the dict(zip(1,2)) function, whereby
 the first array (1) will be the key of the dict and the second will be the values
 The same zip logic of the shortest array/list will apply here aswell and
 as dictionaries cannot have duplicate keys duplicate values of the first array
 will not be in the dictionary.
 """
 
dict(zip(l1,l2))
dict(zip(l3,l4))

"""
 Dictionaries can also be made using dictionary comprehension with a zip(1,2)
 whereby names are declared for key and value such as key: val or ll: ol
 and correspond to array 1 and 2 of the zip.
 """
 
dict1 = {key: val for key,val in zip(l3,l4)}
dict1

dict2 = {key: val for key,val in zip(l1,l2)}
dict2

dict3 = {ll: ol for ll,ol in zip(l1,l2)}
dict3

#And the following is just regular dictionary comprehension in the form
# key: val, it is very similar to set or list comprehension.
dict4 = {x**2: x for x in range(0,5)}
dict4

dict5 = {x:x for x in range(1,7)}
dict5

l5 = [1,2,3,4,5,6]
dict6 = dict(zip(l5,l5))
dict6