# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 19:41:03 2019

@author: Yusef Quinlan
"""

ShoppingList = ["Apples", "Mangoes", "Playstation", "Trout" ] 
                #  0         1            2            3
print(ShoppingList)
NumberList = [3,4,5,6,1,2]
            # 0 1 2 3 4 5
print(NumberList)
MixedList = [3,4,7,1,9,True,False,True, "Arthur", "La rosa", "Machine"]
#The above is a mixed list that shows a list can contain more than one data type
print(MixedList)  
print(ShoppingList[1])  #Print the item at index 1 of ShoppingList
print(NumberList[3])    #Print the item at index 2 of NumberList
print(ShoppingList[-1])  #Print the last item of ShoppingList
print(ShoppingList[-2])  #Print the 2nd-last item of ShoppingList
print(NumberList[2:])   #Print items of index 2 and beyond if NumberList
print(NumberList[2:4])   #Print items of index 2-4 exclusive of 4 from NumberList
print(NumberList[2:5])  #Print items of index 2-5 exclusive of 5 from NumberList

ShoppingList[1] = "Peaches"     #Change item of index 1 in the ShoppingList
print(ShoppingList)
ShoppingList[3] = "Salmon"      #Change item of index 3 in the ShoppingList
Color = ["Blue", "Red", "Yellow"]    
Color.extend(ShoppingList)     
    """ Permanently change the Color list by adding
    The items in ShoppingList to the Color list
    """
print(Color)                
Color.append("Purple")      #Add the colour purple to the Color list
Color.insert(2, 909)        #Insert value 909 to index 2 of Color list
Color.remove("Red")         #Remove value "Red" from the Color list
Color.clear()               #Delete all items in the Color list
ShoppingList.pop()          #Delete the last item in ShoppingList and return it
print(ShoppingList)     
ShoppingList.index("Peaches")   #Get the index number where the item "Peaches" first appears
NumList2 = [1,1,1,2,2,3,4,4]    
NumList2.count(1)               #find out how many times the number 1 appears in NumList2
NumList2.count(3)               #find out how many times the number 3 appears in NumList2
NumberList.sort()               #Sort the NumberList in ascending order
print(NumberList)
print(ShoppingList)
ShoppingList.reverse()          #Put the ShoppingList into reverse order
ShoppingList2 = ShoppingList.copy()    
 #Makes a copy of the ShoppingList and assigns it to variable ShoppingList2