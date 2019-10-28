# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:17:23 2019

@author: Yusef Quinlan
"""

elf_names = ["Jose", "Fernadez", "Maria", "skven","njard", "Skvald"]
print(elf_names)
elf_names2 = elf_names.copy()   #Copy list
print(elf_names2)
elf_names2[1] = "Cyrius"   #Change index 1 of elf_names2
elf_names2[2] = "Sophia"   #Change index 2 of elf_names2
ValuesList = ["lop",99,34,True,False]
ValuesList[-1] = elf_names2   
#Make Last item in ValuesList equal to the value of the elf_names2 list
ValuesList[0] = elf_names2   #change index 0 of ValueList
ValuesList[0] = " "          #Change index 0 to a space
ValuesList.remove(" ")      #removes first space character i.e. index 0
ValuesList.reverse()        #Reverses the order of ValuesList
ValuesList.clear()          #Clears ValuesList
ValuesList.append(33)       #Append 33 to the now cleared ValuesList

