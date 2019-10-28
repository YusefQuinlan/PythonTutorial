# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 15:40:46 2019

@author: Yusef Quinlan
"""

Set1 = {1,7,"Hello"}

#Set creation i.e. put items in '{}' those squiggly brackets 

print(Set1)

Set1.add(8)

#Adding items to the set, notice if you use the command several times the number
# 8 will still only appear in the set once as Sets do not allow duplicate values

list1 = [9,8,23]
Set1.add(list1)

#Lists for some STRANGE Reason, cannot be added to sets

tup1 = (3,4,5)
Set1.add(tup1)

#Tuples however can be added to sets

Set1.pop()

#Gets rid of the first item in a set 

Set1.remove(1)

#remove the item with value 1 in the set, if used when the item is not present in the set
# an error will occur, the remove function is as follow  set.remove(argument)
# if the value that is used as an argument is not in the set an error will occur

Set1.discard(7)

#remove the item with value 1 in the set, if used when the item is not present in the set
# nothing will be removed, the discard function is as follow  set.discard(argument)
# if the value that is used as an argument is not in the set an error will occur

Set2 = {9, 62, 33, "Happy_Days"}
print(Set2)
Set2.clear()

#Using the clear function to clear a set of all items

Set3 = set(list1)

#Makes a set out of a list by converting an existing list into a set

print(Set3)

Set4 = {4,4,4,99,99,9,9}

#Making a set with several values that are the same and assigning it to a variable
# is completely valid, but when you print the set or inspect it after assigning it,
# it will not contain duplicate values even though it appeared to have been assigned them.

print(Set4)
Set5 = Set4.copy()

#Copying of a set

Boolval1 = True #And therefore has a value of 1
Boolval2 = False #And therefore has a value of 0

Set6 = {False,True,1}
#Showing that True has a value of 1
print(Set6)

