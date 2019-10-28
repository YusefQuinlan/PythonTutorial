# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:05:55 2019

@author: Yusef Quinlan
"""

#Import the module named 'math'
import math

"""
A module in python is a file made up of python code, it may contain classes and
also several functions, modules are ussually built for a specific purpose i.e.
there may be a math module like this one, a fishing module online, a physics
module etc, the possibilities are endless. Don't worry too much about what a 
module is at this stage, this is just a side-note that may become important
later on.
"""

#create the variables
A = 22
B = 9.1
C = -12
D = -0.5
E = 102.3
F = 99

print(A * B + C)  #188.2 should be printed
print(A * (B + C)) #-63.80000000 Should be printed out
print(D * C * E * F)
print(E / B * A - B) #238.21868131868135 should be printed
print(E / (B * A - B)) #0.5353218210361067 Should bre printed out
print(A**2) #484  or 22^2
print(A**3) #10648  or 22^3
print(F%A) #Remainder of 11, when 99 is divided by 22 hence return value is 11
print(9%5) #Remainder of 4
print(max(F,A)) #Max value of 99 should be returned as F is 99 and is higher than A (22)
print(min(E,C)) #Min value of -12 should be returned as C is -12 and lower than E (102.3)
print(abs(C)) #12 Returned
print(abs(B)) #9.1 Returned



"""
Learners should try and make their own variables and play around with the maths
functions that have been demonstrated in video 1.5.1 and video 1.5.2, this will
help learners to develop an understanding of how equations are interpreted in python
depending on the placement of parenthesis and also encourages learners to write
code for themselves rather than rely on copy and pasting code.

For further learning it is advised to look at the math module description and
perhaps try some of the math functions not covered in 1.5.1 and 1.5.2
"""