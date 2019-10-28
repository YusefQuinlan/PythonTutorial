# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 16:11:19 2019

@author: Yusef Quinlan
"""

#While something is true..... Do this here
#I.e. while condition is true, exuecute this code

"""Below I/we shall create two while loops, one that prints out the a number ,
 if the number becomes more than 99 then a boolean of name "Less_Than_100"
shall be declared False and boolean of variable name "More_Than_99_Less_than_200" will be declared
to be True , 
A second while loop will increment and print this number,  once the number is more than 199
the variable named "More_Than_99_Less_than_200" will be declared False and the second loop will stop running
both loops increment the number providing it is less than 100 for the first loop and less than 200 
for the second loop, they will print this number at each increment till the conditions are not met
"""

#Assigning the variables
Less_Than_100 = True
num = 0
More_Than_99_Less_than_200 = False

#While loop 1
while Less_Than_100:
    print("Less_Than_100 Loop num is equal to: " + str(num))
    num = num +1 
    if num > 99:
            Less_Than_100 = False
            More_Than_99_Less_than_200 = True

#While loop 2
while More_Than_99_Less_than_200:
    print("More_Than_99_Less_than_200 Loop num is equal to: " + str(num))
    num = num + 1
    if num > 199:
        More_Than_99_Less_than_200 = False
        
#Simpler while loop, this runs whilst The temperature is cold, in the United Kingdom
# 20 degrees celcius is considered warm, at least by me!

#declare variable Cold and temp(stands for temperature and no temporary)
Cold = True
temp = -12

#While loop terminates while when temp > 20 as this make  boolean 'Cold'  False.
while Cold:
    print("its cold, its " + str(temp) + " degrees celcius, put the heating up!")
    temp = temp + 1
    if temp > 20:
        Cold = False


