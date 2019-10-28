# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 17:03:05 2019

@author: Yusef Quinlan
"""
#The below code introduces a concept i.e. that the user can give us an input and we want
#the int value of the input, but there is also potential for error here as users can give 
#inputs that cannot be converted to integer values, and that is what we want to deal with here
number = int(input("Please type in a number:  "))
print(number)

#The try/except clause is introduced here as a means to give feedback or perhaps deal with an error
#in this case the 'ValueError' i.e. the error whereby a user types in a string that cannot be converted
#to an integer, is dealt with by informing the user that their text is invalid.   
try:
    number = int(input("Please type in a number:  "))
    print(number)
except ValueError:
    print("Invalid number, type a number next time, not a word!")
#the below code does the same as the above but as the error 'ValueError' is not declared as the
#error type to be excepted, the except statement will catch most errors in most circumstances    
try:
    number = int(input("Please type in a number:  "))
    print(number)
except :
    print("Invalid number, type a number next time, not a word!")
    
#try: 
#Generic code to be attempted/tried
#except ERROR(The error we are looking for) or except:
# Exception code

#The following shows us how to get items from lists within lists, it is not the optimal solution to
# this problem and will cause an error if the list is altered or the range is altered in
# some circumstances
listp = [[1,2],[1,2],[1,2]]

#the below shows us that we can catch the 'IndexError' that might occur, and tells us to
# 'Sort out our code!' because we can do better than this
for i in range(0, 3):
    print(listp[i])
    for i2 in range(0,2):
        print(listp[i][i2])
        
listp = [[1,2],[1,2],[1,2]]

try:
    for i in range(0, 4):
        print(listp[i])
        for i2 in range(0,3):
            print(listp[i][i2])       
except IndexError:
    print("Something went wrong! Sort your code out!")

#The following shows that we can catch the Error without declaring the error type in the
# except statement.    
try:
    for i in range(0, 4):
        print(listp[i])
        for i2 in range(0,3):
            print(listp[i][i2])       
except :
    print("Something went wrong! Sort your code out!")    

#The following shows that syntax errors in the code of the try statement cannot be excepted

try:
    Fingers = 10 True
except SyntaxError:
    print("Invalid syntax you fool!")