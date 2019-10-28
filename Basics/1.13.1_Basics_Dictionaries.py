# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 18:23:04 2019

@author: Yusef Quinlan
"""

# animalDictionary-----      animalname : Animal Description
# PlantDictionary-----   plantname : Plant Description

Dictionary1 = {}
#Making an empty Dictionary with the {}  squiggly braces
print(Dictionary1)
type(Dictionary1)

Dictionary2 = {"Cat":"A four legged majestic cute furry animal", "Dog": "A loyal and loving pet",
               "Eagle": "Some crazy scary bird that for some reason Americans love????" }
#Making a non-empty dictionary with a key value pair, notice that the item to the left of a 
#Semi-colon is a key and the item to the right is a value, each key-value pair is seperated by a ','

print(Dictionary2)
Dictionary2["Cat"]
Dictionary2["Dog"]
Dictionary2["Turtle"]
#The values of the keys can be accessed in the manner above, but only if the keys exist, otherwise
#an error will occur.

Dictionary2.get("Cat")
Dictionary2.get("Dog")
Dictionary2.get("Turtle")
#The values of the keys can be accessed in the manner above, if the key doesn't exist an error will
#not occur, but a value of 'none' will be returned

Dictionary2.keys()
#Returns a list of all the keys in Dictionary2 (or any dictionary it is used on)
# Dictionary.key()
Dictionary2.values()
#Returns a list of all the values in Dictionary2 (or any dictionary it is used on)
# Dictionary.values()

Dictionary2["Dog"] = "A four-legged creature with sharp teeth that is carnivorous"
#Changing the value assigned to an existing key, however if the key doesn't exist then the
#key will be added to the dictionary and paired with the assigned value, in this case dog is
#not added, but the value associated with it is changed.
print(Dictionary2)
Dictionary2.values()

Dictionary2["Turtle"] = "A four legged reptile with a strong shell on its back"
#Changing the value assigned to an existing key, however if the key doesn't exist then the
#key will be added to the dictionary and paired with the assigned value, in this case the key
# "Turtle" was added to the dictionary and the description will be paired to it as its value
Dictionary2.keys()
Dictionary2.values()
print(Dictionary2)

Dictionary2["Nin"] = [2,3,4,5,6,7]
#Showing that a key can be assigned a list as a value.
Dictionary2.keys()
Dictionary2.values()
print(Dictionary2)

Dictionary2[99] = 562
#Showing that a key can be an integer and that a value can also be an integer
Dictionary2.keys()
Dictionary2.values()
print(Dictionary2)

Dictionary2[88] = 562
#Shows that whilst dictionaries cannot have duplicate keys they can have duplicate values.
Dictionary2.keys()
Dictionary2.values()
print(Dictionary2)