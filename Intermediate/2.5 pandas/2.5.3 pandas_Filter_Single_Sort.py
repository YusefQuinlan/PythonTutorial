# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 18:32:40 2021

@author: Yusef Quinlan
"""

#import and reading of csv file
import pandas as pd 
sc_df = pd.read_csv('Scores.csv')

"""
    In pandas DataFrames, rows can be selected and filtered based on the one of
    the column values for such rows. For example one could get all the rows 
    where the 'Score' value is equal to 3, these rows could then be saved to
    a variable or further manipulated. This is achieved by use of the .loc
    attribute on a DataFrame, basically using the DataFrame name, column name
    and the value to be filtered. As shown in the following code segment:
        Df.loc[Df['ColumnName'] == FilteredValue]. 
"""
sc_df.loc[sc_df['Score'] == 3]
sc_df.loc[sc_df['Score'] > 3]
sc_df.loc[sc_df['Name']== 'Afsana']
sc_df.loc[sc_df['Sex'] == 'm']

"""
    pandas DataFrames can be sorted by columns, for example if the DataFrame 
    needs to be sorted by the Score values in ascending order, this can be 
    achieved, DataFrames can also be sorted by several columns in ascending
    or descending order. The following shows how to sort by one column:
        df.sort_values('ColumnToSortBy')
    By default the DataFrame is sorted by ascending order, it can be sorted
    by descending order using the following :
        df.sort_values('ColumnToSortBy', ascending=False)
    The by argument allows us to sort by multiple columns and the columns
    need to be put into a list. By default they are both sorted by ascending
    order, they can be sorted by descending with an 'ascending=False' argument.
    However, in order to make them ascend differently rather than all by the 
    same ascension, ascensions can be specified in a list for each column name.
"""

sc_df.sort_values('Score')
sc_df.sort_values('Score', ascending=False)
sc_df.sort_values('Name')
sc_df.sort_values('Name', ascending=False)
sc_df.sort_values(by=['Name','Score'])
sc_df.sort_values(by=['Sex','Name'])
sc_df.sort_values(by=['Sex','Name'], ascending=False)
sc_df.sort_values(by=['Sex','Name'], ascending=[False,True])

# The describe function simply provide basic statistical analysis for a DataFrame
sc_df.describe()


