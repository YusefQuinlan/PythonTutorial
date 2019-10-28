# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 18:26:31 2019

@author: Yusef Quinlan
"""
listuno = [1,1,1,1,1]
listdos = [2,2,2,2,2]
# == is the computers way of asking if the item on the left is equal to the item on the right
# = is the computers way of saying that the thing on the left is now equal to the value on the right
def List_appen(n,list1,list2):
    if n == 1:
        list1.append(n)
    elif n == 2:
        list2.append(n)
    else:
        print("This number is neither 1 nor 2 and cannot be appended to either list")
#Shows a few things, how lists can and other items can be interacted with by use of if block
#Shows that you must pay attention to indents i.e. all code is indented once due to defining of function
#Some of the code is indented a second time by the if/elif/else statements.
        
List_appen(1,listuno,listdos)
#Testing our code.

if 1 > 2:
    print("1 > 2")
elif 4 > 5:
    print("4 > 5")
elif 8 > 9:
    print("8 > 9")
#Shows that more than one elif can be used in an if block and that else is not needed in an if block

if 9 < 12:
    print("7 < 12")
if 8 > 7:
    print("8 > 7")
#Shows that the 'if' keyword always starts a new if block and two if statements i.e. 'if'
# Keywords cannot be part of the same if block.
    
if 8 > 9:
    print("if fired!")
elif 8 > 12:
    print("first elif fired!")
elif 8 < 9:
    print("second elif fired!")
else:
    print("else statement fired!")
#Shows how one can find out easily which if/elif/else statement condition has been met.

    