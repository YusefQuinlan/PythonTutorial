# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 12:36:27 2021

@author: Yusef Quinlan
"""

#import pandas and read the csv file
import pandas as pd
sc_df = pd.read_csv('Scores.csv')

#check the DataFrame.
sc_df

"""
    Here df.loc has been used to find all scores of value 2, after the 2 a 
    comma has been placed, this actually signals a column argument and the
    column 'Score' is used, after this the assignment operand is used, and the
    value 3 is assigned to all row values of 2 in the Score Column.
"""
sc_df.loc[sc_df['Score'] == 2,'Score'] = 3
sc_df

# Making of random numbers to be used for newly added columns.
nonvals = [i for i in range(0,19)]
print(nonvals)

# New column made with the nonvals values as default values.
sc_df['Rating'] = nonvals
sc_df['Rating']

"""
    Here df.loc has been used in a similar manner only this time it filters
    based on scores of above 5, the argument used after the filtering for
    the column is 'Rating'. This means that the rating column rows will be 
    altered to be the value after the '=' i.e. 'good' for any rows that contain
    the value of Scores above 5 i.e. the 'Score' conditional.
"""
sc_df.loc[sc_df['Score'] > 5, 'Rating'] = 'good'
sc_df

# Similar to above.
sc_df.loc[sc_df['Score'] < 5, 'Rating'] = 'bad'
sc_df.loc[sc_df['Score'] == 5, 'Rating'] = 'Okay'
sc_df

# New column made with the nonvals values.
sc_df['Comment'] = nonvals
sc_df

"""
    Similar to the other uses of df.loc, the only difference is that a list
    of columns has been used as the argument after the conditional, and changes
    will be made to bthe rows of both these columns where the conditional is
    met. This list can have as many columns as exist in the DataFrame.
"""
sc_df.loc[sc_df['Score'] >= 8, ['Rating','Comment']] = 'Excellent'
sc_df