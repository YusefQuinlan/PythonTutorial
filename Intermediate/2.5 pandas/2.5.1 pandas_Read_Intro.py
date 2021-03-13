# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 17:37:34 2021

@author: Yusef Quinlan
"""

#Standard pandas import, pip install if you don't have pandas
import pandas as pd

# Reading the csv file into a pandas DataFrame using read_csv on the filepath
# in this case filepath is relative. Print(scores_df) prints the DataFrame
scores_df = pd.read_csv('Scores.csv')
print(scores_df)

# Printing the head and tail of the DataFrame (First or last 5 entries)
print(scores_df.head())
print(scores_df.tail())

# Reading an excel file rather than a csv file using pd.read_excel('filename')
# Relative path, printout the new DataFrame and its head and tail.
scores_df2 = pd.read_excel('Scores.xlsx')
print(scores_df2)
print(scores_df2.head())
print(scores_df2.tail())
