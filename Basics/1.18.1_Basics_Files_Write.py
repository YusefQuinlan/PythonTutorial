# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 18:39:13 2019

@author: Yusef Quinlan
"""
#Here/below the open function opens a file depending on the file path and the second argument
# determines what will be done to the file, w is for write, a is for append and r is for read
# if a file doesnt exist and the chosen mode is 'w' then the file will be written to existence
#if the file exists it will be overwritten
#the .write("String") method, writes the string to the file
#.close() is used to close the file so that changes can be made permanent
Friend_file = open("friends.txt","w")
Friend_file.write("My first friend is Sameer")
Friend_file.close()

#When examining friends.txt you will see that the file will have been overwritten and contain
#the text "My first friend is Rupert" and not the text "My first friend is Sameer"
Friend_file = open("friends.txt","w")
Friend_file.write("My first friend is Rupert")
Friend_file.close()

#This code shows that write() can be used several times, however without a \n 'newline' special
#character, the text will not be written to a new line
Friend_file = open("friends.txt","w")
Friend_file.write("My first friend is Rupert")
Friend_file.write("My Second friend is Sameer")
Friend_file.close()

#The following shows the new line character will work (examine friens.txt after running the code)
Friend_file = open("friends.txt","w")
Friend_file.write("My first friend is Rupert")
Friend_file.write("\nMy Second friend is Sameer")
Friend_file.close()

#the following codes shows a way to write multiple lines with just one function i.e. writelines()
Friend_file = open("friends.txt","w")
Friends_Lines = "My first friend is Rupert", "\n my second is Sameer", "\n My third friend is Samantha"
Friend_file.writelines(Friends_Lines)
Friend_file.close()

#Here the "a" mode is used as an argument to the open() function, this means we intend to append to
#the file used as the first arguments, note that nothing will be overwritten with the append mode.
Friend_file = open("friends.txt", "a")
Friend_file.write("\n My Fourth friend is Aneesh")
Friend_file.close()

#Just further demonstration of the append mode.
Friend_file = open("friends.txt", "a")
Friend_file.write("\n My Fifth friend is chen long")
Friend_file.close()