# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 10:46:14 2021

@author: Yusef Quinlan
"""
#importing both pandas and numpy
import pandas as pd
import numpy as np

# reading an excel file and checking the resultant DataFrame.
sc_df = pd.read_excel('Scores2.xlsx')
sc_df

"""
    The df.dropna() function returns a DataFrame that doesn't contain any rows
    who have at least one NaN (np.nan data type) value. As can be seen this
    does not change the original DataFrame.
"""

sc_df.dropna()
sc_df

"""
    The df.dropna() function argument defaults are axis='index' and how='any',
    this means that it deletes indexes i.e. rows, and how it deletes them is
    that it deletes a row that contains 'any' NaN values. When the how 
    value is changed to 'all' no rows are deleted, this is because 'all' only
    deletes where all values are NaN, and there is no row in the DataFrame with
    all NaN values.
"""

sc_df.dropna(axis='index', how='any')
sc_df.dropna(axis='index', how='all')

"""
    The following df.dropna() functions are now used on columns, the first
    will drop any columns that contain at least one NaN value, as all columns
    contain at least one NaN value, the first one drops all columns and returns
    an empty DataFrame. The second line doesn't drop any columns, this is
    because none of the column have all NaN values.
"""
sc_df.dropna(axis='columns', how='any')
sc_df.dropna(axis='columns', how='all')

# The DataFrame has not been altered.
sc_df

# the DataFrame is altered now due to the inplace=True argument.
sc_df.dropna(axis='index', how='any', inplace=True)
sc_df

# Reseting the sc_df DataFrame to original values.
sc_df = pd.read_excel('Scores2.xlsx')
sc_df

"""
    Here the replace function is used on the entirety of the DataFrame and
    replaces all values 'Unknown' with 'Missing', not that this changes the
    DataFrame as inplace=True is used.
"""
sc_df.replace('Unknown', 'Missing', inplace=True)
sc_df

# Same as above but 'Missing' is replaced by NaN values.
sc_df.replace('Missing', np.nan, inplace=True)
sc_df

# df.isna() returns all NaN values as True for a DataFrame.
sc_df.isna()

"""
  df.fillna(arg) allows us to replace all NaN values with a specified argument,
  in this case with the word missing, it doesn't change the DataFrame.
"""  
sc_df.fillna('Missing')
sc_df

# Same as a bove but changes original DataFrame due to inplace=True argument.
sc_df.fillna('Missing', inplace=True)
sc_df

#df.dtypes allows us to see what datatype each column implements.
sc_df.dtypes

"""
    Loading the original 'Scores.csv' file as our DataFrame, looking at the 
    dtypes it can be seen that Score has been default implemented as int
    due to all Scores being ints, but Age is implemented as an object,
    this is because one of the values in that column is a string and not an
    integer, so pandas default made that column of type 'object' rather than
    integer.
"""
sc_df = pd.read_csv('Scores.csv')
sc_df.dtypes
sc_df

# Changing the Age that is a string to an integer..
sc_df.loc[18, 'Age'] = 35
sc_df

"""
    The 'Age' column datatype is still object even though the string was 
    changed to an integer, this is because the datatype for the entire column
    has not been changed, only for one item. Below the whole column is 
    converted to integer with the astype(int) function with int as an argument.
"""
sc_df.dtypes
sc_df['Age'] = sc_df['Age'].astype(int)

"""
    Here is can now be seen that the datatype for the Age column is now an 
    integer, and the mean can be extracted from it.
"""
sc_df.dtypes
sc_df['Age'].mean()
