# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:22:06 2020

@author: Yusef Quinlan
"""

Array1 = [3,4,7,8,9,"p","l",True]

# Slicing is when you take out a slice of an array to be used, rather than
# use the whole array

#Prints out 3, a small slice of our array.
print(Array1[0])

#Prints an array of the array that includes 0 - 7 exclusive of 7
print(Array1[0:7])

# Prints an array of the array that includes 0 -8 exclusive of 8 (whole array)
print(Array1[0:8])

# Prints from array item 0 to end array item i.e. 0 - end, represented [0:]
print(Array1[0:])

# Prints items 2 - 5 i.e. third item to the fifth item, arrays start at zero
# [2 is the start inclusive: 5 is the end item and is not included]
print(Array1[2:5])

# Prints the array items in an array from item 0 to item -1
# i.e. the first item up till the last item minus 1.
print(Array1[0:-1])

# Prints array items in an array from item 0 to item -2
# i.e. the first array item up till the last item minus 2
print(Array1[0:-2])

# Prints an array with items 0 to minus 1 of the first array, but only includes every
# second item (including [0]) as the third argument dictates the increment
print(Array1[0:-1:2])

# Prints an array that includes all items of the first array that are third items
# from the first item i.e. position 0,3,6 of the array.
print(Array1[0::3])

# Does the same as the above and proves that 0 is the default first argument
# and that the default second argument is to the end of the original array
print(Array1[::3])

# Prints an array with all items from first array item 2 to  item 0,
# it is in inverse order because the increment argument is negative.
print(Array1[2::-1])

# Same as above but starts at 4 and ends at 1
print(Array1[4:1:-1])

# prints all in reverse order
print(Array1[-1::-1])

# Proves that strings can be sliced.
print("hello"[1:])

"""
The slicing arguments are as follows:
    [Start-point(inclusive):end-point(exclusive):increment]
The defaults are as follows:
    [0:the end of array:1]
    
negatives increment values will reverse the increment and you will get items
in reverse order, if an increment is higher than one you will get every xth
item for example 2 will give every second item from the start point up till the
end point. -2 would give you every second item backwards from the start point
up till the end point, if the end point is higher than the start point, the
slice will take everything from the start point backwards at the specified 
increment
"""