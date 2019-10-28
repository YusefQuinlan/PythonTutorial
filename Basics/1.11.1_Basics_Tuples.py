# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 14:27:05 2019

@author: Yusef Quinlan
"""
#     tuples

tup1 = (9,"Hello World", True, 8,8,3) #Making a tuple
# Variable name =  Parenethesis(Values...)

print(tup1)

List1 = [9,"Hello World", True, 8,8,3]
print(List1)
#List with same values as tup1

List1.append("Cool")
#items can be appended to Lists but they cannot be appended to tuples
#In fact a tuple cannot be altered or change in any way and is said to be 'immutable'

Tup_list = [tup1,"hello"]
#A Tuple data structure can be an item in a list
Tup_list[0] = 99
#An item in a list can be changed
print(Tup_list)

Tup_list[0][0] = 99
#but an item inside a tuple cannot be changed, the [0][0] refers to index 0 of list for the first [0]
#and then index 0 of the item of at index 0 of the list i.e. [0] of tup1
#Item at [0][0] cannot be changed as it is inside a tuple and tuples are immutable/cannot be changed

tup2 = (3,5,6,9)
print(tup2)
list2 = list(tup2)
print(list2)
list2.append(11)
tup3 = tuple(list2)
print(tup3)
#The above shows how even though tuples cannot be changed, lists can be and simple conversion between
#the two data structures can be a work around for immurable/unchangeable data structures.