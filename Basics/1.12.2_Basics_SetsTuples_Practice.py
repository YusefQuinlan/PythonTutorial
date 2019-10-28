# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 17:12:52 2019

@author: Yusef Quinlan
"""

Tup1 = ("Lol","Lol",9,2,3,True,False)
#Tuple creation (Tuples cannot be altered in any way)

print(Tup1)

List1 = list(Tup1)

print(List1)
List1[0] = "Hello Mundo!"
List1.append("huevos!")
print(List1)
Tup2 = tuple(List1)
print(Tup2)

#The above shows how to make a new tuple that is an edited version of an old tuple
# Rather the old tuple has not been edited but a list copy of it has been
# the list copy is then converted to a new tuple

Set1 = {34,22,55,99,True}
print(Set1)

#Set creation, sets must not have duplicate values

Set2 = set()
#Creation of an empty set, empty sets cannot be created using   an empty'{}' set of brackets
# This is because instead a dictionary is created, a dictionary is another data structure
# It is not the same as a set 

Set2.add(9)

#If the add command is used more than once no duplicate entries will be added to the set
print(Set2)
Set2.discard(9)
#remove a set item
Set1.add(34)

Set1.pop()
#Delete set item 1 i.e. index 0 item

Set3 = {1,1,1,1,1,1,1,1,1,1,1}

#Even though the set creation looks as though it would create several duplicates it does not
#As sets may not contain duplicates.

print(Set3)

