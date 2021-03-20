# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 14:35:39 2021

@author: Yusef Quinlan
"""

# Importing pandas, loading csv and checking the resultant DataFrame.
import pandas as pd
sc_df = pd.read_csv('Scores3.csv')
sc_df

# Here a DataDrame with only the male entries is held in the variable males.
males = sc_df.loc[sc_df['Sex'] == 'm']
males


#Here a DataFrame with only the female entries is held in the variable females
females = sc_df.loc[sc_df['Sex'] == 'f']
females

"""
    The males and also the females DataFrames are now being exported as csv 
    files. This happens by using the to_csv() function on the DataFrames to be
    exported, and using the filename as the argument, note this will write to
    wherever this program is run from and to save it to somewhere specific will
    require a filepath.
"""
males.to_csv('males.csv')
females.to_csv('females.csv')

"""
    The same as above but the DataFrames are written to the tsv file format,
    the .tsv extension must be explicitly named in the argument for the 
    filename. An argument sep='\t' must be used to show that the various items
    are tab seperated.
"""
males.to_csv('males.tsv', sep='\t')
females.to_csv('females.tsv', sep='\t')

"""
 written to xlsx extension the only difference is the extension name and that
 the function used is to_excel, specify the filetype as an xlsx file for this
 to work properly.
"""
males.to_excel('males.xlsx')
females.to_excel('females.xlsx')

