# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 17:11:39 2021

@author: Yusef Quinlan
"""

import pandas as pd

"""
    Making a dictionary to be used to make a pandas DataFrame with.
    The keys are the columns, and the values for the keys (which must be lists)
    are what are used to make the DataFrame.
"""
dictionary1 = {
    'Column1':['val','val','val'],
    'Column2':['Jack','Dentist','lllll'],
    'AColumnName':[1,2,3]
    }

# The dataframe is used with pd.DataFrame(dictionary1).
df = pd.DataFrame(dictionary1)
df

"""
    Here a list of tuples is created and a DataFrame will be created from these
    tuples. Each tuple represents a value of the rows and there are no column 
    names, so column names must be specified later.
"""
Tuples1 = [('val','val2','hello'),
 (4,5,3),
 (99,88,77)]

"""
    Here the pd.DataFrame() function is used with the tuples list as an 
    argument, and also with the column names as an argument and a DataFrame is
    created.
"""
df = pd.DataFrame(Tuples1, columns=['Col1','Tr','MOP'])
df

"""
    Here the columns attribute of our DataFrame is accessed, so that we can see
    all the different columns in our DataFrame. The columns are then edited by
    directly editing the .columns attribute with a list of new column names for
    the existing columns. This will permanently change the column names.
"""
df.columns
df.columns = ['Col1','Mr','Mop']
df

"""
    A list comprehension is used here in order to change the columns attribute
    of our DataFrame, it changes our column names to uppercase versions of
    themselves.
"""
df.columns = [colname.upper() for colname in df.columns]
df

# Same as the above but lower case instead.
df.columns = [colname.lower() for colname in df.columns]
df

"""
    Below, the df.rename() function is used with the columns argument,
    this returns a DataFrame that is a modified version of the original 
    DataFrame. The modifications being that the new column names specified in
    the argument will be the names of the returned columns names. Note that
    not all column names must be changed and that the column names that are to
    be changed must be put as keys in a dictionary and the value to be changed 
    to should be their values. 
"""
df.rename(columns={'col1':'T-rex','mop':'POM'})
df

# Same as above, but with the inplace=True argument, the DataFrame is changed.
df.rename(columns={'col1':'T-rex','mop':'POM'}, inplace=True)
df