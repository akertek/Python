#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 14:15:14 2020

@author: egeakertek
"""

import pandas as pd
import numpy as np

file_name = "movies.xls"

sheet1900 = pd.read_excel(file_name, sheet_name=0)
sheet2000 = pd.read_excel(file_name, sheet_name=1)
sheet2010 = pd.read_excel(file_name, sheet_name=2)

sheet1900_head = sheet1900.head(10)

sheet1900["Sheet"] = 1900

df_movies = pd.concat([sheet1900, sheet2000, sheet2010])


#describe?
df_desc = df_movies.describe()

#%%

# 1916'daki film hangisi?
movie_wanted = df_movies[df_movies["Year"] == 1916]


#%% Clean Duplicates

df_movies_dups = df_movies[df_movies.duplicated(keep = False)]

df_movies.drop_duplicates(keep= "first",inplace = True)

#%% Sort - Gross Earnings

df_earnings= df_movies.sort_values(by = "Gross Earnings", ascending = False)
df_earnings_head = df_earnings.head(10)

#%% 
df_movies["Income"] = df_movies["Gross Earnings"]-df_movies["Budget"]
df_movies_income = df_movies.sort_values(by = "Income", ascending = False)


#%% Hangi yılda kaç film çekilmiş?

ser_count = df_movies["Year"].value_counts()

#%%

df_animation_movies = df_movies[df_movies["Genres"].str.contains("Animation") & df_movies["Genres"].str.contains("Sci-Fi")]
