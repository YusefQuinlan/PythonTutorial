# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 11:03:49 2021

@author: Yusef Quinlan
"""

import pandas as pd
sc_df = pd.read_csv('Scores.csv')

#sc_df['NewCol'] = ?????

"""
    Here two columns rows are aggregated (concatenated technically), put into
    a variable and then added to a newly created column ('NewCol').
    A new column can be made by putting a new column name in brackets after
    a DataFrame. Such as the following:
        DataFrame['columnName'] = whatever the column row values are
    A set of row values needs to be assigned to the column though.
"""
newColVals = sc_df['Name'] + " " + sc_df['Sex']
print(newColVals)
sc_df['NewCol'] = newColVals
sc_df

# New column is added and assigned the values in the vals variable
vals = [4,6,3,2,2,7,9,4,2,3,4,5,7,8,9,5,2,1,3]
sc_df['randVals'] = vals
sc_df

"""
    the DataFrame.drop() function can be used to delete an entire column.
    it is used below with the argument columns=['randVals'] to delete the
    randVals column. The only problem is that if there is no inplace=True
    argument then a new dataFrame without the specified column is returned,
    but the old DataFrame is not updated.
"""
sc_df.drop(columns=['randVals'])
sc_df

"""
 Here the 'randVals' column is removed from the DataFrame due to the 
 inplace=True argument in the drop() function.
"""
sc_df.drop(columns=['randVals'], inplace=True)
sc_df

# adding the randVals column back to the DataFrame after deleting it.
vals = [4,6,3,2,2,7,9,4,2,3,4,5,7,8,9,5,2,1,3]
sc_df['randVals'] = vals

# multiple columns can be deleted if multiple columns are put in a list.
sc_df.drop(columns=['NewCol','randVals'], inplace=True)
sc_df

"""
    The DataFrame.append() function can allow for rows to be added to
    a DataFrame. By using a dictionary with the keys being columns and
    the values being values for that row as an argument and using 
    ignore_index=True as an argument. Unfortunately this does not 
    change the dataFrame and just returns what the changed dataFrame would be
"""
sc_df.append({'Name':'Billy Jay','Score':9}, ignore_index=True)
sc_df

# here the DataFrame is changed as it is assigned the return value of append()
sc_df = sc_df.append({'Name':'Billy Jay','Score':9}, ignore_index=True)
sc_df

# Rows can also be dropped by using their index number as an argument.
sc_df.drop(index=19, inplace=True)
sc_df
