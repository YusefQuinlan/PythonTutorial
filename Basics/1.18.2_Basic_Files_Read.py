# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 19:57:29 2019

@author: Yusef Quinlan
"""
# Simply using the open function and using 'r' as the argument will put a readable variable
# into the Friends_file variable, afterwards the read() function is used to read the file and as per usual
# the close() function is used to close the file
# sometimes the full path of a file needs to be used in order for read to work rather than just the
# filename.
Friends_file = open("friends.txt","r")
print(Friends_file.read())
Friends_file.close()