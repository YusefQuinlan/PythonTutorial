# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 15:38:07 2020

@author: Yusef Quinlan
"""
# What is a generator?
# A generator is an iterable object, that can be iterated over
# but it is not an object that contains all the iterable instances of whatever
# it iterates, at once.

# return will return the first valid value and exit the function
# so the following function wont return the whole range.
def iterablereturn():
    for i in range(9):
        return i

# Returns 0, the first value in range(9) -- 0,1,2,3,4,5,6,7,8
iterablereturn()

"""
A generator essentially makes an iteration formula and produces a generator object
 based on that formula, however the generator does not contain every iteration
 rather it has to be iterated over and each item generated must be used at
 each iteration in order to have value, as a generator can only be iterated 
 over once
"""

# generators use the keyword yield and must be iterated over to be useful.
def yielder():
    for i in range(9):
        yield i

# using the following function will just output a generator object not the
# iterable items that the object can produce, as it does not contain them, rather
# it generates them one by one.  
        
yielder() 

# The following is the correct use of a generator   
for i in yielder():
    print(i)    


aList1 = [x for x in range(9)]
aList2 = [x for x in range(9)]

# The following functions have the same outputs, but differ in their 
# manner of execution, their use of RAM and their efficiency.
def five_list(alist):
    for i in range(len(alist)):
        alist[i] = alist[i] * 5
    return alist

def five_list_yield(alist):
    for i in range(len(alist)):
        yield i * 5

# Checking original list value        
for i in aList1:
    print(i)       

# Proof of outputs 
for i in five_list(aList1):
    print(i)
    
for i in five_list_yield(aList2):
    print(i)

