# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 13:04:58 2019

@author: Yusef Quinlan
"""

Hot = False
Cold = not(Hot)
print(Cold)

Wet = False
Dry = not(Wet)
print(Dry)

Night = True
Day = not(Night)
print(Day)

#On opposite day the value True is actually false because it is inverted, so this is an example of
#  not(True), On opposite day the value False is actually true because it is inverted,
# This is an example of not(False)


value1 = True
value2 = False
Truth_Value = value1 and value2  
print(Truth_Value)
#shows that only if both values are True using an
# 'and' operator can the overall value be True.

value3 = True
value4 = True
Truth_Value2 = value3 and value4
print(Truth_Value2)
#Demonstrates the same as above by using both True and True


Truth_Value3 = 1 < 3 and 5 > 3 and 5 > 4
print(Truth_Value3)
#Shows that more than one 'and' operator can be used, All values must be True.

value5 = True
value6 = False
Truth_Value4 = value5 or value6
print(Truth_Value4)
#Demonstrates the use of 'or' operator, only one of the values used needs to be True

Truth_Value5 = value5 or value6 or value2
print(Truth_Value5)
#Use of several or operators, only one value needs to be True for value to be True

Truth_Value6 = value6 or value2
print(Truth_Value6)
#No value here is False and so Truth_Value6 evaluates to False.

Truth_Value7 = value4 or value6 and value1
print(Truth_Value7)
#Shows use of multiple operators 'or' and 'and' as long as one of the items used by
# the 'or' statement is True and value1 is True the value evaluates to True

Truth_Value8 = (value4 or value6) and (value1)
print(Truth_Value8)
#Demonstrates more clearly how python evaluates with multiple different operators (logical)
#Also shows a way to write code so that you or python do not misinterpret the meaning of the
# logic in the code.

Truth_Value9 = (value2 or value6) and (value1)
print(Truth_Value9)
#Evaluates to False because none of the values used by 'or' are True

Truth_Value10 = not(value2 or value6) and (value1)
print(Truth_Value10)
#Evaluates to True because the inverse of the or boolean value is True.

ASTRING = "i" == "i"
ASTRING2 = "I" == "i"
#The '==' asks if the item on the left is the same as the item on the right if the items are the same
#Then a boolean value of 'True' is produced, otherwise a boolean value of 'False' is produced
#The '=' tells the machine that the variable on the left holds the value of the item on the right


ASTRING = "i" != "i"
ASTRING2 = "I" != "i"
#The '!=' asks the machine if the item on the left is not equal to the item on the right
#If the item on the left is not equal to the item on the right then a boolean value of 'True' is produced
#Otherwise a boolean value of False is produced.


numbool1 = 1 > 2
numbool2 = 1 < 2
# is 1 greater than 2? i.e. is left greater than the item to the right of the '>' symbol
# is 1 lesser than 2? i.e. is left lesser than the item to the right of the '<' symbol

numbool1 = 1 <= 1
numbool2 = 1 <= 0
#is 1  less than or equal to 1/0 i.e. is left item less than or equal to the item to
# the right of the '<=' symbol?

numbool1 = 1 >= 1
numbool2 = 1 >= 2

#is 1 more than or equal to 1/2 i.e. is left item more than or equal to the item to
# the right of the '>=' symbol?