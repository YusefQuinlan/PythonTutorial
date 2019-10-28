# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 16:02:26 2019

@author: Yusef Quinlan
"""

# If x is true : then y happens, else if x is not true then z happens, or nothing happens
#I.e. if it is raining I will wear a jacket, else I will wear a tshirt only
#I.e. if it is raining I will use an umbrella, else I will not use one i.e. nothing happens

Raining = False

if Raining:          #if condition == true then execute this code
    print("it is Raining")
    print("I should wear a coat")
    
Happy = True
    
if Happy:       #if condition == true then execute this code
    print("I am soo sooooooo Happy!    :)")
    
if 3 > 2:       #if the question being answered i.e. 3 > 2 is true then execute code
    print("3 is greater than 2!!!")
    
#If in the above a boolean is given rather than a question asked to produce a boolean
#then the if statement will check to see if the boolean is true or false.
n1 = 9
n2 = 11  
     
if n1 > n2:
    print("n1 greater than n2")
else:
    print("n2 greater than n1")
#The above will print the second print statement in the case that n1 is not greater than n2
#i.e. if the 'if' Statement is not true then the else will be executed i.e. everything else statement

n1 = 11
n2 = 11 
if n1 > n2:
    print("n1 is greater than n2")
elif n1 < n2:
    print("n2 is greater than n1")
else:
    print("n2 is not greater than or lesser than n1")
    
#If is used to introduce a block consisting of possibly just 'if' , an 'if' 'elif', an 'if' 'else' or 
# an 'if' 'elif' 'else' combination, in this case an 'if' 'elif' 'else' combination
# if the 'if' condition is not met then the code will check if the 'elif' condition is met
# if the 'elif' condition is not met, then the else code will execute as it covers all posibilities
# other than the if or elif statement/s above it.
    
    
    
nu1 = 1
nu2 = 1


if nu1 > nu2:
    print("nu1 greater than nu2")
elif nu1 < nu2:
    print("nu2 greater than nu1")
elif nu1 == 1:
    print("nu1 is of value 1")
else:
    print("I have no idea what is going on!!!")
    
#the above block shows that after the initial if statement to start the code block,
# several elif statements can be used in the same if/elif code block or
# if/elif/else code block.    