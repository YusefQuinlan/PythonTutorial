# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 16:49:29 2019

@author: Yusef Quinlan
"""

# A loop is a bunch of instructions/ an instruction that repeats itself if/while a condition holds true
# If a loop is not properly constructed and its condition stays True, it may loop infinitely
# We can design the loops to stop looping once they have achieved something useful.

grapes_in_hand = 0

while grapes_in_hand != 10:
    print("I have " + str(grapes_in_hand) + " grapes in my hand!"  )
    grapes_in_hand = grapes_in_hand + 1
#The above loop executes while grapes_in_hand is not equal to int value 10,
#Therefore if the grapes_in_hand value ever becomes equal to 10 the loop will stop
#And so the loop will stop printing and increasing the value of grapes_in_hand
#Since grapes_in_hand is increment by 1 (1 is added to the value) in every instance/iteration
#Of the loop, and also starts with a value of 1, it will eventually reach a value of 10 and
#Therefore the loop will stop executing. Because the condition 'grapes_in_hand not 10' or
# 'grapes_in_hand != 10' is no longer True.

grapes_in_hand = 0
while grapes_in_hand != 10:
    print("I have " + str(grapes_in_hand) + " grapes in my hand!"  )
#This loop will execute forever (Or until you run out of RAM perhaps) because the value of
#grapes_in_hand is never changed within the loop, therefore it will always be of value 0
# and will never be equal to 10 hence this loop runs forever because the condition
#    'grapes_in_hand != 10'           will always be True

grapes_in_hand = 1
while grapes_in_hand != 10:
    print("I have " + str(grapes_in_hand) + " grapes in my hand!"  )
    grapes_in_hand = grapes_in_hand + 2
#This loop is also an infinite loop because whilst grapes_in_hand has been incremented, it has been
# over-incremented, because it starts with a value of 1 and never reaches the value 10, it reaches
#the value 9 and then the value 11, and then loops infinitely as it never becomes equal to 10
# and so the condition is not broken, this is an example of bad loop design.    

    
grapes_in_hand = 1
while not(grapes_in_hand >= 10):
    print("I have " + str(grapes_in_hand) + " grapes in my hand!"  )
    grapes_in_hand = grapes_in_hand + 2
#This loop is similar to the loop above it, but in order to resolve the increment problem
# it will terminate if there are more than ten grapes in hand and shows better design of a while loop


grapes_in_hand = 1 
Handsize = False    
while not(Handsize):
    grapes_in_hand = grapes_in_hand + 1
    print("I have " + str(grapes_in_hand) + " grapes in my hand!"  )
    if grapes_in_hand >= 10:
        Handsize = True

#Shows that regular booleans can be used rather than just expressions that produce a boolean
# It also shows that if statements can be used inside of a while statement and that one value can
# affect a boolean condition. It is an un-neccessarily complex design though.

    