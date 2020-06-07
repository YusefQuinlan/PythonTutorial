# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 21:28:24 2020

@author: Yusef Quinlan
"""

# What is Scope?
# Scope is the context/area in which a variable exists, or in which
# anything exists.

x = 11
print(x)
x = x + 1
print(x)

# Trying to modify the existing x with a function
def xplus1():
    print(x + 1)
    x = x + 1
    
# Notice that the function does not execute and the print(x) shows no change in
# the value of x. This is because the x created outside the function is not
# used inside the function/ is not within the scope of the funciton.
    
xplus1()
print(x)

# This following function allows us to use the variable x declared outside of 
# it with the keyword 'globa' followed by the variable name 'x'
# With this declaration x is now within the scope of the function.
def xplus2():
    global x
    x = x + 2

# Running the function and a print statement confirms that x value has been 
# altered by the function.    
xplus2()
print(x)

# yinit attempts to create a variable 'y' and prints its value
def yinit():
    y = 9
    print(y)

# Notice that yinit() prints out a value of 9, but the print statement of
# print(y) after the function gives a 'name "y" is not defined error
# this is because although y is defined within the function, the function
# does not make y exist outside of its scope.
    
yinit()   
print(y)

# yinit2() attempts to do the same as yinit(), however y is created as a 
# variable outside of yinit2() since it has been declared as a global variable.
def yinit2():
    global y
    y = 9
    print(y)

# Now the second printout clearly shows that y is initialised with a value of
# 9 by the yinit2() function. The global declaration has worked.
yinit2()
print(y)