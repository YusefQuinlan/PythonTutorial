# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 12:06:29 2021

@author: Yusef Quinlan
"""

import pandas as pd
sc_df = pd.read_csv('Scores.csv')

# look at the DataFrame
sc_df

# get the names of the columns in list form.
col = list(sc_df.columns.values)
col

"""
    the df[col[2:4] + col[0:2]] line will return the df DataFrame
    in the following column order: col[2],col[3],col[0],col[1] ,rather than
    the default:  col[0],col[1],col[2],col[3] using the values from
    the col list. This is then assigned to the DataFrame and so the
    DataFrame is re-ordered.
"""
sc_df[col[2:4] + col[0:2]]
sc_df = sc_df[col[2:4] + col[0:2]]
sc_df

"""
    Instead of taking multiple columns a more specific order can be given
    with individual columns, but they must be put in [] brackets before
    concatenation.
"""
sc_df = sc_df[[col[0]]+ [col[2]] + [col[3]] + [col[1]]]
sc_df