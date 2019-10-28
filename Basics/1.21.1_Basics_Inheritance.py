# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 23:08:33 2019

@author: Yusef Quinlan
"""
#Creation of a class with just one function
class Anyclass:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def get_name(self):
        return self.name
#testing get_name function on an Anyclass object 
AObj = Anyclass("An Obj", 92)
AObj.get_name()

#Creating Anyclass2 by passing the Anyclass class as an argument 
# Anyclass2 will inherit all the attributes and functions of Anyclass,
# But a new function such as print_cool can be added to the class.
class Anyclass2(Anyclass):
    def print_cool(self):
        print("Cool!")

#Confirming that functions of Anyclass have been inherited by Anyclass2 by testing them
# on Anyclass2 objects, also testing of the print_cool() function        
Obj2 = Anyclass2("David", 76)
Obj2.print_cool()
Obj2.get_name()

#Demonstrating that the print_cool() function doesn't work on Anyclass objects
# Because the function is unique to Anyclass2
AObj.print_cool()

#Defining a reptile class
class reptile:
    def __init__(self, name, legs, canSwim):
        self.name = name
        self.legs = legs
        self.canSwim = canSwim
    def get_all(self):
        print("name: " + str(self.name) + "\n" + "Legs : "+ str(self.legs) + "\n",
              "canSwim : " + str(self.canSwim))

#testing functions of a reptile class        
lizard1 = reptile("iguana", 4, True)
lizard1.get_all()

#Making a class for a specific reptile i.e. Lizard class
class Lizard(reptile):
    def WhatIAm(self):
        print("This animal is a lizard!!!")

#testing functions of the Lizard class.        
lizard2 = Lizard("iguana",4, True)
lizard2.get_all()
lizard2.WhatIAm()