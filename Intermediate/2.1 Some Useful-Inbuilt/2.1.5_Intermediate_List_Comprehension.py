# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 18:23:54 2019

@author: Yusef Quinlan
"""
a = [1,4,9,6]
#in the following 3 lines all the values from one list multiplied by 2; are
# added to another list in the traditional way via a for loop.
b = []
for n in a:
    b.append(n * 2)
    
print(b)
"""
With list comprehension it is possible to get all the values of one list 
 multiplied by two into another list with just one line of code. This list 
 comprehension follows the following format:

NewList = [Algorithm for x in array/range]
an algorithm is used an applied to either numbers of a range or items of an 
array; the result of this algorithm for each item is added to the new list.
""" 

twos = [x * 2 for x in a]
print(twos)

#Here list comprehension is used to get all items in the the ten times table 
# from 0 x 10   up to 9 x 10
tens = [i * 10 for i in range(0,10)]
print(tens)

# Here list comprehension gives us the square of all the values from 0 - 9.
Squared = [x ** 2 for x in range(0,10)]
print(Squared)