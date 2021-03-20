# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 13:52:11 2021

@author: Yusef Quinlan
"""

import pandas as pd
sc_df = pd.read_csv('Scores3.csv')

sc_df

"""
    The groupby() function allows for the grouping of certain items in a column
    for example grouping the ['Sex'] column will split it into its unique
    values i.e. its groups m and f (male/female). However it needs an 
    aggregate function to be applied to it in order to be useful. The
    mean() function will get the various means for the groups in the ['Sex']
    column, i.e. the mean Age and Score for males and for females.
    This can be sorted further with the .sort_values('Columname') function.
"""
sc_df.groupby(['Sex']).mean()
sc_df.groupby(['Sex']).mean().sort_values('Score')

"""
    Here the same aggregate functions and the same sorting is used, but it
    is now grouped by the ['Age'] Column.
"""
sc_df.groupby(['Age']).mean()
sc_df.groupby(['Age']).mean().sort_values('Score')

# the sum() aggregate gives a sum of all the values for grouped items.
sc_df.groupby(['Sex']).sum()

"""
    The count() aggregate gives a count of how many times a grouped item 
    appears in a row, in this case some ages appear multiple times
    in various rows, but names only appear once each. This show that are 
    duplicate ages split among several rows, but that all names are unique.
"""
sc_df.groupby(['Age']).count()
sc_df.groupby(['Name']).count()

# The groupby function can be applied to more than one Column.
sc_df.groupby(['Age','Sex']).mean()