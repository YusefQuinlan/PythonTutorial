# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 13:37:09 2019

@author: Yusef Quinlan
"""
#Creating a list to show that a list is an object and represents a real list
# such as for example a shopping list, and a list has properties such as allowing
#items to be added to it
list1 = [1,2,3,4,5,6]
Shoppinglist = ["Oranges","oil","Curry"]

#Declaring the class PersonalInformation
#inside the class self refers to the object being created or operated on by a function
# i.e. an object of type PersonalInformation
# PersonalInformation class contains the number, age and name properties
# init that is defined below allows us to initialise a PersonalInformation object
# (create one) with the arguments phoneNumber, Age and Name.
# the argument value used for phonenumber sets the self.number property, argument value used for Age
# sets the self.age property, the argument value used for Name sets the self.name property
class PersonalInformation:
    def __init__(self,phoneNumber,Age,Name):
        self.number = phoneNumber
        self.age = Age
        self.name = Name

#below PersonalInformation objects are created using the construction function of PersonalInformation
# i.e. PersonalInformation(phoneNumber, Age, Name)
Johnny = PersonalInformation("09778961",22,"Johnny Castello")
print(Johnny.age)
Sarah = PersonalInformation("393848735",97,"Saz the legend!")
print(Sarah.name)

#Someclass class is defined and shows that we can intialise properties of a class
# without defining there value in the constructor argument i.e. Sclass.number2 = 99, this is set without
# using an argument to set it.
class Someclass:
    def __init__(self, number):
        self.number = number
        self.number2 = 99
        self.string = "aString"
        
Sclass1 = Someclass(905)
print(Sclass1.number)
print(Sclass1.number2)
print(Sclass1.string)

#Showing that properties of custom class objects in a list can be viewed with use of class.property
# or more specifically list[indexofobject].property
PIlist = [Johnny, Sarah]
PIlist[0].age 

#This is a class whos constructor has no arguments.
class frog:
    def __init__(self):
        self.legs = 4
        self.height = "10cm"
        self.length = "22cm"
        
frog1 = frog()
frog1.length