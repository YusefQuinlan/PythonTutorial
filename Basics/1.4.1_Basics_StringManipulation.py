# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 10:49:51 2019

@author: Yusef Quinlan
"""

StringContainer = "Fighting"
StringContainer.upper()                #Should return an uppercase version of variable StringContainer
StringContainer = StringContainer.upper()  #Changes the variable permanently into an uppercase version of itself.
print(StringContainer)
StringContainer.lower()    #Should return a uppercase version of variable StringContainer
StringContainer = StringContainer.lower()  #Changes the variable permanently into a lowercase version of itself.
print(StringContainer)
StringContainer.isupper() #Returns True if all characters of StringContainer are uppercase
StringContainer.islower() #Returns False if all characters of StringContainer are lowercase
StringContainer.upper().isupper() #returns value True
StringContainer.upper().islower() #returns value False
len(StringContainer)    #Returns the length of the string in variable StringContainer
StringContainer[2]      #Returns item at index 2 of the String in StringContainer
StringContainer.index("ti")    #Returns index of string "ti" in StringContainer
StringContainer.replace("Fi","Lo")  #Replaces "Fi" with "Lo"
