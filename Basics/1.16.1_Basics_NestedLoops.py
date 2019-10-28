# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 18:28:37 2019

@author: Yusef Quinlan
"""

#A nested loop, is a loop within a loop

#The following is a nested loop the code in the first loop will execute 7 times
# the code in the second loop will execute 21 times because it executes 3 times for every
# iteration of the first loop
for i in range(0,7):
    print(i + 1)
    for i2 in range(0,3):
        print(i2 + 1)

#The following is a small exercise with some print outs to show how many times the code
# in each loop has executed        
num = 1

for i in range(0,7):
    print("This is iteration number: " + str(i +1) + " of the first loop" )
    for i2 in range(0,3):
        print("This is iteration number: " + str(num) + " of the second loop")
        num = num + 1

#The following also shows how many times code in each loop has executed and it also
# Demonstrates that any kind of loop can be put inside any other kind of loop        
num1 = 1

for i in range(0,10):
    print("this is iteration number: " + str(i + 1) + " of the first loop")
    while ((i + 1) * 10) > num1:
        print("this is execution number : " + str(num1) + " of the code in the second loop")
        num1 = num1 + 1

#The following also demonstrates how many times code in each loop is executed
# The formula is that each consecutive loop shall be executed x times (where x is 
# the number of iterations of that loop) times by the amount of times the previous loop executes
# i.e. if loop1 (the main loop) executes 10 times, then loop2 with 10 iterations should execute 100 times
# i.e. 10 x 10, and loop 3 should execute 1000 times i.e. 10 x 100 or more accurately 10 x 10 x 10 times.
count1 = 1
count2 = 1
for i in range(0,10):
    print("this is iteration number: " + str(i + 1) + " of the first loop")
    for i2 in range(0,10):
        print("this is execution number : " + str(count1) + " of the second loop")
        count1 = count1 + 1
        for i3 in range(0,10):
            print("this is execution number : " + str(count2) + " of the third loop")
            count2 = count2 + 1
            
