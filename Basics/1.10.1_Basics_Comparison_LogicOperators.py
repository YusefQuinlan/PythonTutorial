# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 19:57:56 2019

@author: Yusef Quinlan
"""

# is 1 smaller than 7???
# yes,         1 < 7
#   7 > 1

#          ==   the double equal sign asks if the item on the left is equal to the item on the right
#      1 == 3, is really a question of 'is 1 equal to 3?' i.e. is left equal to right?
# single = says that the item on the left (a variable?) is equal to the item on the right
# i.e. Variable1 = 99  is saying to the machine that the variable named 'Variable1'
#Now holds a value of 99 as an integer.

Variable1 = 99
print(Variable1)

if 1 == 3:
    print("1 is equal to 3!")
    
if Variable1 == 99:
    print("Variable1 is equal to 99!")
    
if Variable1 == 72:
    print("Variable1 is equal to 72!")
    
#    !=   this asks the machine, is the item on the left not equal to the item on the right?
# if the item on the left is not equal to the item on the right, then boolean value True is returned
    
if 1 != 3:
    print("1 is not equal to 3")
#^ Is 1 not equal to 3?     !=
    
if 3 > 2:
    print("3 is greater than 2")
 #Is 3 greater than 2?     >
if 2 < 3:
    print("2 is less than 3")
 #Is 2 less than 3?    <
if 2 >= 1:
    print("2 is greater than or equal to 1")
if 2 >= 2:
    print("2 is greater than or equal to 2")
if 2 >= 3:
    print("2 is greater than or equal to 2")  

#Is the item on the left more than or equal to the item on the right??   >=

if 4 <= 5:
    print("4 is less than or equal to 5")
if 4 <= 4:
    print("4 is less than or equal to 4")
if 3 <= 2:
    print("3 is less than or equal to 2")
    
#Is the item on the left less than or equal to the item on the right??   <=   

if 3 > 1 and 1 < 2:
    print("3 is less than 1 and also 1 is less than 2")
if 1 > 2 and 1 < 2:
    print("1 is more than 2 and less than 2")
if 1 > 2 and 1 < 0:
    print("1 is more than 2 and less than 0")
if 1 > 0 and 1 > -1 and 1 > -1:
    print("success, all three truth conditions met!")
    
#and is asking if two or more comparison question answers are true
# i.e is the answer on the left and the answer on the right True?
#are the boolean values of all these compared statements true?
    
if 1 > 0 or 1 < 0:
    print("1 is more than zero or it is less than zero")
if 1 < 0 or 1 < -1:
    print("1 is less than zero or one is less than -1")
    
#Are one of these answers on the left or the right True?
# is one of the comparison statements True i.e. boolen val of True?
    
boolVal = not(True)
print(boolVal)
boolVal2 = 1 > 0
print(boolVal2)
#Not(Boolean) makes the boolean value inside the brackets the opposite value
# Boolean values can be assigned to variables by use of comparisons rather than strict
#Assignemt of True or False

if not(1 > 3):
    print("1 is not Greater than 3")
    
#if I am not hot then I am cold
# Am I hot???
# if I am not hot then not hot = true, therefore if cold then hot = False i.e. Not(hot) is True
    
Cold = True
Hot = not(Cold)