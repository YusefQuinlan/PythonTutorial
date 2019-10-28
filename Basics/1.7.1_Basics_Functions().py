# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:54:39 2019

@author: Yusef Quinlan
"""

print("Ger")

#   FunctionName  ---   Parenthesis () 
# function()
# FunctionName --- parenthesis (Argument)
# Function(argument)
#   an example is a print statement i.e. print is the name of the function
#this name is followed by a parenthesis then inside the parenthesis is an argument
# i.e. the text/number/value/values that we want to print

print(55)
    
def Small_Speech():
    print("This is the jolly speech!")
    print("We are the jolly people!")
    print("We come to bring joy to the lands!")
    print("We come in peace we come in joy, o praise thee!")
    print("May joy prevail!")

#note that to define a function the keyword 'def' must be used before the function-name
#Also note that anything inside the function must be indented.
Small_Speech()
#test your functions as I have done above
def Small_Speech2(Name, number):
    print("This is the Jolly Speech of " + Name)
    print(Name + " Has given speeches " + str(number) + " times")
#Functions may have arguments that can be used by the function such as the name and number argument.
    
Small_Speech2("Damon",55)
#Once again TEST your functions.


