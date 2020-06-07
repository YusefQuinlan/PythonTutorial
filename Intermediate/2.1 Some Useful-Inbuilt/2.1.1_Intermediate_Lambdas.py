# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 09:56:50 2019

@author: Yusef Quinlan
"""

def squared(x):
    return x * x

squared(100)

# A lambda function is an anonymous function, it can have several arguments
# it is only one line long, and it always returns a value.


#the names before the colon are the arguments/argument, anything after
# that will be returned by the lambda.
"""
lambda x: x * x
lambda x: x + x
lambda x, y: y + x
lambda x,y,z, etc: .....................
"""
#Creation of lambda will result in a object returned as the function is anonymous
# as a result a function object will be returned.
lambda x: x * x

#Lambdas can be assigned to variables.
sq = lambda x: x * x
#Should get 400 back as the return value
sq(20)

# A lambda can have multiple arguments.
lambda x,y: x + y

add = lambda x,y: x + y

add(9,10)

#if you uncomment the 'x +8' you will get an error as lambdas can only work on one line
lambda x : x + 5
#x + 8

#Notice that the lambda works with any data type that could be manipulated by its
# specified function.
add("Hello ", " World!")