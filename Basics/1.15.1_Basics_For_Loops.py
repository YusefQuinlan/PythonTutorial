# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 17:33:19 2019

@author: Yusef Quinlan
"""
# A loop is code that repeats until a condition is met that stops the code from repeating
# A computer game is a loop, it keeps running until you shut it down or turn of the game
# The condition for it to stop running is that either the console it is on is shut down or
# The game itself is shut down.
"""
 A for loop is a loop that is run a pre-selected amount of times
 In a for loop where we want to print the word dave 5 times, we declare how many times
 we want the code to run and set up the code of the loop as has been done below
Note that the value of times/i is the same as the loop number when using the 
 in range method.
"""

for times in range(0,5):
        print("dave")
        print("range number is : " + str(times))

#Below  the number 1 is doubled 7 times by use of an in range for loop
        
num_doubled = 1

for doubling in range(0,7):
    print(num_doubled * 2)
    num_doubled = num_doubled * 2
    
#Below every item 'in list_x' is printed, note that since we are iterating(looping)
#through a list/collection the i/item value is the value of the item at the index
# number of the loop iteration and is not the loop number.
list_x = [3,7,8,9]

for item in list_x:
    print(item)

#Changing every item in a list to have an int value of '10' by using in range
# With the first number starting at zero and the last value being the length
# of the list we want to change, note that because of the in range method the item/i
#value is the loop number/ the loop iteration.
for item in range(0, len(list_x)):
    print(item)
    list_x[item] = 9

#This will produce an error because the value of 'item' is 9 in this list however
#  list_x has no index of value 9, its highest index number at this point is 3
# The index os out of the range of the list in this case.
    
for item in list_x:
    list_x[item] = 99

#The below will append the int value of '10' to the List 'List_new_1000_tens'
# 1000 times and print the proof of such.
List_new_1000_tens = []
for i in range(0,1000):
    List_new_1000_tens.append(10)
    
print(List_new_1000_tens)