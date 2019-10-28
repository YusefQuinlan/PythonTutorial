# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 19:51:03 2019

@author: Yusef Quinlan
"""

Dictionary1 = {}
#creating of an empty Dictionary
print(Dictionary1)
type(Dictionary1)

Dictionary1[33] = 453
Dictionary1[33] = 563
#showing that we cannot have duplicate keys
Dictionary1[99] = 563
#Showing that we can have duplicate values even though we cannot have duplicate keys.
print(Dictionary1)

Dictionary1.clear()
#Clears the dictionary i.e. erases the dictionary of all its items.

Tool_Dict = {"Hammer":"A hammer is used to nail things into a wall or smash a coconut", "Knife":
    "A knife can be used to slice food and also to open boxes", "Scissors":
        "Scissors can be used to cut things open"}
#Dictionary with actual keys and key-value pairs
Tool_Dict.keys()    
#Shows all the keys in the Tool_Dict Dictionary, using the keys() function
Tool_Dict.values()
#Shows all the values in the Tool_Dict Dictionary, using the values() function
Tool_Dict["Can-opener"] = "Used to open up tin cans"
#Shows that by editing a non-existing key, the key will be added to the Dictionary
#Along with the value entered for its key-value pair
Tool_Dict.keys()    
Tool_Dict.values()
#Checking the keys and the values
Tool_Dict.pop("Can-opener")
#Getting rid of the "Can-opener" key.
Tool_Dict.keys()    
Tool_Dict.values()
Tool_Dict.get("Hammer")
#Accessing the value of the Hammer key i.e. the description of a Hammer

Likes_Dict = {"Martial arts":"Love martial arts since watching kung-fu movies",
              "Number 9": 9, True:"I don't like liars"}
#Making another dictionary that uses A boolean as a key and an int as a value of a key-value pair
Likes_Dict.keys()
Likes_Dict.values()
#checking the dictionary values and the dictionary keys
Likes_Dict.items()
#Checking the key-value pairs of the dictionary
Likes2_Dict = Likes_Dict.copy()
#Making a copy of the Likes_Dict   Dictionary.
Likes2_Dict.items()

Likes2_Dict.update({"Bananas":"I just love bananas, gotta get that Pottassium!",
                   "Linasa":"Linasa means linseed in Spanish", "Python":
                   "I absolutely love the python programming language"})
#The update function is called update because it can update several existing keys in a dictionary,
#This is achieved by entering the key-value pairs with only the values altered, the values will then be
#updated. If non-existent keys are used they and their values will be added to the dictionary as
#key value-pairs, thus the update function offers a convenient way to add several key-value pairs to
# a dictionary
    
    
# Dictionary.Update({dict_key1:dict_value1, dict_key2:dict_value2})    
Likes2_Dict.keys()
Likes2_Dict.values()  
#Check the keys and the values after updating the Dictionary.