# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 19:36:01 2021

@author: Yusef Quinlan
"""

# pandas import and reading of the csv file
import pandas as pd
scores_df = pd.read_csv('Scores.csv')

"""
 printing out the columns of the DataFrame using the .columns attribute
 Shows the names of all the columns for the scores_df DataFrame.
 the column names are put into a variable for future use (Hypothetical)
"""
print(scores_df.columns)
col_names = scores_df.columns

"""
    All the values for a specific column can be retrieved using the
    column name in brackets after the name of the DataFrame whose column
    values are being retrieved, for example:
    DataFrame['ColumnName'] 
"""
print(scores_df['Name'])
print(scores_df['Age'])

"""
    Column values can also be taken using the column name attribute after
    dot notation on a DataFrame such as:
        DataFrame.columname
    Several values can be taken by adding a slice bracket after
    the column name bracket.
    multiple columns values can be taken by using a list inside the bracket
    that comes after the database and desired column names can be put
    in said list.
"""
print(scores_df.Name)
print(scores_df['Name'][0:4])
print(scores_df[['Age','Score']])

"""
    DataFrame.iloc[n] gets the row with the index value 'n', specific
    columns of specific rows can be retrieved using either the column
    index as an argument i.e. df.iloc[n,columnIndex] or by asking for
    the column name after the iloc in the following format:
        df.iloc[n]['columname']
""" 
print(scores_df.iloc[3])
print(scores_df.iloc[2])
print(scores_df.iloc[0:3])
print(scores_df.iloc[3]['Name'])
print(scores_df.iloc[3,1])
print(scores_df.iloc[3,0])

# Row being stored in a variable.
asf = scores_df.iloc[1]
print(asf)
