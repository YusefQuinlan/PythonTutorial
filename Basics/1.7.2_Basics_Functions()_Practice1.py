# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 12:26:57 2019

@author: Yusef Quinlan
"""
#FunctionName --- () Parenthesis
#    Function()
#FuntionName --- (Argument) Parenthesis
#   Function(Argument)

def Fun():
    print("*********")
    print("3333")
    print("rjighutrgijtrg")
#Defining a function with name Fun by using the def keyword and indentation of
#the code to be executed in the function    
Fun()
#Testing the function
def Fun2(name):
    print("Your name is: " + name)
#Function with an argument
Fun2("Johnny")
#Testing the function
Der = Fun2("Johnny")
#Demonstrating that the print function returns no value
def Fun3(name, age):
    stri1 = "Your name is: " + name + " and you are " + str(age) + " years old"
    return stri1
#A function Fun3 that uses arguments and a return statement
Der = Fun3("Maria", 33.5)

def Sum_Num(num1, num2):
    num3 = float(num1) + float(num2)
    return num3
#Return statement once again being used
mynum = Sum_Num(5,10)

def Generate(age):
    print("You look handsome for a " + str(age) + " yr old!")
    Person_age = "this person is " + str(age)
    return Person_age
    
Darwens_age = Generate(93)

def Gen2(NUM1):
    NUM2 = NUM1 * NUM1 * NUM1
    return NUM2
    print("hello world!")
#demonstrating that lines inside the function that are written after the return statement,
#Will not be read nor used.
Gen2(33)


    