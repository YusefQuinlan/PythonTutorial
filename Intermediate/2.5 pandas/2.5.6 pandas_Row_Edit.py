# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 18:04:42 2021

@author: Yusef Quinlan
"""

import pandas as pd
sc_df = pd.read_csv('Scores.csv')

#checking the DataFrame in general
sc_df

"""
    Here the row at index 3 is located to see what it is and contains,
    after being observed, it is changed by using the assignment operator '='
    on it. On the left side of the assignment operator a list containing the 
    values for all the row values can be seen, and these values will be the 
    new calues for the columns of the row.
"""
sc_df.loc[3]
sc_df.loc[3] = ['22','Afsana','f',9]

# checking that changes have been applied.
sc_df.loc[3]

"""
    Here instead of getting and changing the entire row at index 2, a second
    argument is added to the df.loc() function, this is a list of all the 
    columns that are to be altered, on the right of the '=' operator, two
    values are put into a list and the column values selected for that row
    will be chaged to be those two values. A second loc() function is used to
    confirm that changes have been applied.
"""
sc_df.loc[2, ['Age','Score']] = ['29',9]
sc_df.loc[2]

# Here just one column is changed so lists are not needed.
sc_df.loc[6, 'Age'] = '23'
sc_df.loc[6]

"""
    Here a row is retrieved using a filter, the DataFrame is filtered by the
    'Name' column for the name 'Malik', and any rows returning such name are
    returned by the filter.
"""
varFilt = (sc_df['Name'] == 'Malik')
sc_df.loc[varFilt]

"""
    Here the filter is used as an index argument (since it only returns one 
    result as true), and the Malik row is updated with the filter.
"""
sc_df.loc[varFilt, 'Score'] = 7
sc_df.loc[varFilt]