# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 14:24:09 2019

@author: Yusef Quinlan
"""

# A nested loop is a loop inside a loop
# There can be several loops inside loops, inside loops.

#The algorithm below demonstrates a times table where the times tables for all numbers
#From 1 to 12 are printed out, i.e. 1 x 1, 1 x 2 to 1 x 12 (for one) up to 12 x 12
Times_Table = 12

for i in range(0, Times_Table):
    for i2 in range(0,Times_Table):
        print(str((i + 1) * (i2 + 1)) + " is number: " + str(i2 +1) + " in the " + str(i +1) + " times table")

#The algorithm below demonstrates the algorithm above but with a different value for 
# the 'Times_Table' variable, the algorithm is not perfect and the second loop should perhaps
# show range(0, set_number) where 'set_number' is a set number that is not a value taken
# from the 'Times_Table' variable.
Times_Table = 11

for i in range(0, Times_Table):
    for i2 in range(0,Times_Table):
        print(str((i + 1) * (i2 + 1)) + " is number: " + str(i2 +1) + " in the " + str(i +1) + " times table")        

#The algorithm below shows that nested loops can be used to get the values of items
#within a list within a list.        
Ourlist = [[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]]  

for i in range(0,5):
    print(Ourlist[i])
    for i2 in range(0,3):
        print(Ourlist[i][i2])

#The algorithm below shows that the algorithm above was imperfect and that one should always
#think about how they are implementing their code, the use of the last value of range
# being the length of 'Ourlist' and 'Ourlist[i]'(in the second loop) is a better implementation.        
Ourlist = [[1,2,3],[1,2,3],[1,2,3],[1,2]] 

for i in range(0,len(Ourlist)):
    print(Ourlist[i])
    for i2 in range(0,len(Ourlist[i])):
        print(Ourlist[i][i2])