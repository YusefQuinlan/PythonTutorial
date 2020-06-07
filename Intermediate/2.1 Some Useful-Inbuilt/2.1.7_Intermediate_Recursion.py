# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 12:51:42 2020

@author: Yusef Quinlan
"""

#What is a recursive function?
#A recursive function is a function that calls itself.

# A basic recursive function with no Base case
def recursiveFunc():
    print("I am recursive")
    recursiveFunc()
    
recursiveFunc()

# a base case is a condition that allows a recursive function to stop calling itself

def stringRev(String):
    if len(String) > 1:
        return stringRev(String[1:]) + String[0]
    else:
        return String
    
stringRev("tin")

# our first called function is stringRev("tin"), and we called it.
# our second called function is stringRev("in") and it is called within our first call.
# our third and last called function is stringRev("n") and it is is called within our second call.

# the first and second call cannot return String[0] until the StringRev(String[1:]) calls
# are resolved.
#once the third call is resolved, it returns "n"
# this allows the second calls stringRev("n") to resolve and so the second call returns
# stringRev("n") which is "n" plus the first item in the string "in" i.e. "i"
# so the second call returns "n" + "i" i.e it returns "ni"
# the first calls stringRev("in"), returns "ni" and the String[0] of "tin"
# returns "t", so the first call returns "ni" + "t", i.e. "nit"
# and this is why "tin" is returned from stringRev("tin")

def numOutput(num):
    if num < 20:
        print(str(num) + " is the final number and is less than 20 ")
    else:
        print(str(num) + " is our number and is 20 or more")
        numOutput(num -5)
        
        
numOutput(36)
