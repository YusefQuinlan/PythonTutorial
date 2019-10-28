# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:33:19 2019

@author: Yusef Quinlan
"""
Korpor = "Peter is 7, Peter is short, Peter is male" #Original String
Korpor = "Peter is 7 \nPeter is short \nPeter is male"   #\n starts a new line in a String
print(Korpor)
LongString = "Gerry thinks he is \"77\" years old" # \ is the escape character
print(LongString)
Concatenated = "Kilts and " + "Whisky" #Demonstrates Concatenation
Addition = 99 + 1   #Demonstrates numerical addition
print(Concatenated)
print(Addition)
Concatenated2 = "99" + "1"  #Demonstrates that string Concatetion will be used on Strings rather than addition
print(Concatenated2)
On = "OnOnOnononon"
print(On)
print(On.replace("OnOnOn","Phiz"))  #Demonstrates replacing of values in String
Porky = "Peter, hfghehfuir Peter, Peter,v fkrkbferig, Peter"
print(Porky.replace("Peter","Danniella"))   
print(Korpor.replace("\n",""))
FiveChar = "treni"   #Exercise to help understand how arrays/Strings etc start at 0 in Python.
           #01234
print(FiveChar[4])
print(len(FiveChar))
