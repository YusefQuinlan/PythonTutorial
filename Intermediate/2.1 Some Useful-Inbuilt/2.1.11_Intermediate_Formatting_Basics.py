# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 11:36:37 2020

@author: Yusef Quinlan
"""

# What is formatting?
# Formatting is a way of adding strings locked in variables/ arrays
# to another String

String1 = "aaaaaaaaaaaaaaaaaaa"
String2 = "bbbbbbbbbbbbbbbbbbb"

"""
 String1 and String2 are added to new string to the parts where the {} brackets
 are present, in the .format() function the variables are added in order of
 bracket appearance, i.e. argument 1/ variable 1 relates to bracket 1 and
 argument 2/ variable 2 relates to bracket 2. 
"""

New_String = "the first String is {}, the second String is {}.".format(
              String1, String2)

# checking our formatting with a print statement
print(New_String)

"""
 Here we reverse the order of the variables in the .format() argument to prove
 that the order of the arguments of the format function relates to the order 
 in which the brackets {}  are inserted, the variable replace the corresponding
 brackets.
"""

New_String2 = "The second String is {}, and the first String is {}.".format(
        String2, String1)
# Checking that this has worked as intended.
print(New_String2)

# making a dictionary whose items shall be added to a String via formatting.
Dict1 = {'Name':'Pedro Hernandez', 'age':32}

# Dictionary items can be added by using their values as .format() arguments
# once again the first argument replace/correspend to the first bracket {}
# and so on and etc.
New_String3 = "Your name is {}, and your age is {}".format(
        Dict1['Name'], Dict1['age'])

# Checking that this has worked as intended.
print(New_String3)

# names can be put into the brackets and defined in the .format() arguments.
New_String4 = "Your name is {name}, and your age is {age}".format(
        name=Dict1['Name'], age=Dict1['age'])

# Checking that this has worked as intended.
print(New_String4)

# Items can be pulled from a list if the list and the index is used as an argument.
List1 = [45, 650]
New_String5 = "The amount of cows on the farm is {}, and there are {} sheep".format(
        List1[0], List1[1])

# Checking that this has worked as intended.
print(New_String5)

"""
Another way to format Strings is to use the letter 'f' followed by the String
this only works with python version 3.6 and beyond. And brackets need to have
a variable name inserted into them, rather than being blank, strings in brackets
can be modified via functions that would normally modify strings such as
String.upper() or String.lower() etc.
"""

# using f with a list index as an argument.
New_String6 = f"The amount of cows on the farm is {List1[0]}"

# Checking that this has worked as intended.
print(New_String6)

# using f with a variable as an argument.
New_String7 = f"The first String is {String1}"

# Checking that this has worked as intended.
print(New_String7)

"""
 f can also accomodate multiple lines of strings and format them, but the 
 Strings must be put in parenthesis and seperated line by line for this to 
 work, they all need to start with an f and cannot be a mix of f formatted
 strings and unformatted strings.
"""

New_String8 = (
        f"The first String is {String1} "
        f"The second String is {String2}"
        )

# Checking that this has worked as intended.
print(New_String8)

# Proving that variables inside brackets {} can be modified in f formatting.
New_String9 = f"The first String is {String1.upper()}"

# Checking that this has worked as intended.
print(New_String9)