# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 19:14:39 2019

@author: Yusef Quinlan
"""
#In the class 'twoValues' a function called 'compareOneAndTwo' has been written that compares
# the value1 and value2 attributes of the class, the function prints out appropriate text
# depending on which value is higher.

class twoValues:
    def __init__(self, value1):
        self.value1 = value1
        self.value2 = 50
    def compareOneAndTwo(self):
        if self.value1 > self.value2:
            print("Value1 is greater than value2")
        elif self.value1 == self.value2:
            print("Value 1 is the same as value2")
        elif self.value1 < self.value2:
            print("Value 1 is less than value2")

#Creation of several objects of type twoValues, each with accompanying print statements
# to show their attribute values.
obj1 = twoValues(100)
print(obj1.value1)
print(obj1.value2)
obj2 = twoValues(49)
print(obj2.value1)
print(obj2.value2)
obj3 = twoValues(50)
print(obj3.value1)
print(obj3.value2)

#execution of the compareOneAndTwo function on the objects.
obj1.compareOneAndTwo()
obj2.compareOneAndTwo()
obj3.compareOneAndTwo()

#the class Pinfo is defined here with two functions, one is get_name and the other is set_name
# these are getter and setter methods, get_name returns the name attribute of Pinfo objects, and 
#set_name sets the name attribute of Pinfo objects. Setters and getters are very useful for
# changing already set attributes and also to observe the values of attributes in a class.
class Pinfo:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        
    def get_name(self):
         return self.name
     
    def set_name(self, newName):
        self.name = newName

#Creation of a Pinfo object and demonstration of setter and getter functions (set_name and get_name)  
# on those objects.
        
NoName = Pinfo(46, "Timmy")
print(NoName.age)
NoName.get_name()
NoName.set_name("Timothy")
print(NoName.name)
NoName.get_name()

#Demonstrates that the function compareOneAndTwo() cannot be used on objects of type Pinfo
# because the function is a function defined in the twoValues class and not the Pinfo class.
PinfoAllValues = Pinfo(33,99)
PinfoAllValues.age
PinfoAllValues.name
PinfoAllValues.compareOneAndTwo()
