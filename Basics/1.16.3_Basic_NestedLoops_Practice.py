# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:10:45 2019

@author: Yusef Quinlan
"""

# A nested loop is a loop within a loop
# there may be more than one loop within a loop, and there may be loops within loops
# within loops etc etc
# Any type of loop can be put into any other type of loop


#as in the example below, several loops can be put into one loop without being put into another
# i.e. in the below example the two loops with range(0,3) are both with the loop with range(0,5)
# and so are nested in that loop, but they are both independant of eachother and are not nested within
# eachother.
for i in range(0,5):
    print(i+1)
    for i2 in range(0,3):
        print(i + 1 + (i2 + 1))
    for i3 in range(0,3):
        print(i + 1 + (i3 + 1))

#The below shows that you can use any type of loop within another type of loop
whilenum = 1        
for i in range(0,10):
    while whilenum < ((i+1) * 3):
        print("Whilenum is equal to: " + str(whilenum))
        whilenum = whilenum + 1

#The below demonstrates how quickly nested loops can multiply/add to the amount
# of overall lines of code actually run by your program, for those who want to do more homework
# there is something called 'Big O notation' that goes into this concept in more detail than I.
#for those of you who are curious to see the multiplicative effects of nested loops
# you may want to mess about with the value of 'Amount_Times' and experiment to see what happens
# you could change the value to a rediculous number such as 1000 or 10,000  , be warned though
# your computer may not be able to handle it and I bear no responsibility for any damages you might
# incur by experimenting with the variable value. 
num1 = 1
num2 = 1
Amount_Times = 10

for i in range(0,Amount_Times):
    print("iteration number: " + str(i+1) + " of the first loop")
    for i in range(0,Amount_Times):
        print("execution number: " + str(num1) + " of the code in the second loop")
        num1 = num1 + 1
        for i in range(0,Amount_Times):
            print("execution number: " + str(num2) + " of the code in the third loop")
            num2 = num2 + 1
            
