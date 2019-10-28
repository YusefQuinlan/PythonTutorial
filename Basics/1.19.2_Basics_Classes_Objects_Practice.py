# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 17:07:41 2019

@author: Yusef Quinlan
"""
#Defining a Snake class with a no argument constructor

class Snake:
    def __init__(self):
        self.eyes = 2
        self.tail = True
        self.venemous = False

#Declaring the Python variable of type Snake.
        
Python = Snake()
print(Python.eyes)
print(Python.tail)
print(Python.venemous)

#Defining another snake class with a no argument constructor
class Snake2:
    def __init__(self):
        self.eyes = 2
        self.tail = True
        self.venemous = True
        
#Declaring the Viper variable of object type snake       
Viper = Snake2()
print(Viper.eyes)
print(Viper.tail)
print(Viper.venemous)

#Defining another snake class that does have an argument in its constructor
# to determine and set wether or not the Snake object is venemous.
class Snake3:
    def __init__(self, VenomState):
        self.eyes = 2
        self.tail = True
        self.venemous = VenomState

#Declaring the Python variable using an argument in the constructor
Python = Snake3(False)
print(Python.eyes)
print(Python.tail)
print(Python.venemous)
#Declaring the Python variable using an argument in the constructor
Viper = Snake3(True)
print(Viper.eyes)
print(Viper.tail)
print(Viper.venemous)

#Errors will occur with the first class because the value of self.property is never assigned.
class TestClass:
    def __init__(self):
        self.property 
        self.property2 = 0

class TestClass:
    def __init__(self):
        self.property = ""
        self.property2 = 0
        
TestVariable = TestClass()