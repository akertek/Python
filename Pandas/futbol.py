#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 16:29:16 2020

@author: egeakertek

Python ve pandas ile futbol verisi incelemesi.
- q1 [ ] en çok farklı skor ile bilen 10 mac
- q2 [ ] en çok fol atilan 10 mac
 
- q3 [ ] en çok mac oynamis sahir
- q4 [ ] en çok mac oynamis ulke
 
- q5 [ ] en çok gol atan takim
- q6 [ ] en az gol yiyen takim
 
- q7 [ ] en uzun yenilmezlik unvani
- q8 [ ] her turnuva tipindeki mac sayisi
"""

#%%
import time
import numpy as np
import pandas as pd

df_scores = pd.read_csv("results.csv")

#%% Friendly olmayanları çıkart.

df_scores_imp = df_scores[df_scores["tournament"] != "Friendly"]
#%% Şehirlerle ülkeleri ayır.

df_scores[['City', 'Country']] = df_scores["city"].str.split(",", expand=True)

#%% q1 [ ] en çok farklı skor ile bilen 10 mac

df_scores["Goal Difference"] = abs(df_scores["home_ft"] - df_scores["away_ft"])

df_sorted_by_gt = df_scores.sort_values(by = "Goal Difference", ascending = False)



#%%  q2 [ ] en çok fol atilan 10 mac

df_scores["Total Goals"] = df_scores["home_ft"] + df_scores["away_ft"]

df_sorted_by_total_goals = df_scores.sort_values(by = "Total Goals", ascending = False)

#%% - q3 [ ] en çok mac oynamis sehir

city_count = df_scores["City"].value_counts()

#%% - q4 [ ] en çok mac oynamis ulke

country_count = df_scores["Country"].value_counts()

#%% - q5 [ ] en çok gol atan takim

country_forward = {}
    
for index, row in df_scores.iterrows():
    
    if row["home_team"] not in country_forward:
        country_forward[row["home_team"]] = 0
    if row["away_team"] not in country_forward:
        country_forward[row["away_team"]] = 0
    
    
    country_forward[row["home_team"]] += row["home_ft"]
    country_forward[row["away_team"]] += row["away_ft"]

df_country_forward = pd.DataFrame(list(country_forward.items()),columns = ['Country','Goals Forward']) 

df_country_forward_sorted = df_country_forward.sort_values(by = "Goals Forward", ascending = False)

# İkinci ve kolay bir yol 
home_team = df_scores["home_ft"].groupby(df_scores["home_team"]).sum()
away_team = df_scores["away_ft"].groupby(df_scores["away_team"]).sum()
en_cok_golatan = (home_team+away_team).sort_values(0, ascending=False)

#%% - q6 [ ] en az gol yiyen takim

country_against ={}

for index, row in df_scores.iterrows():
 
    country_against[row["home_team"]] =  country_against.get(row["home_team"], 0) + row["away_ft"]
    country_against[row["away_team"]] =  country_against.get(row["away_team"], 0) + row["home_ft"]

# df_country_against_sorted = sorted(country_against,key = country_against.get)

df_country_against = pd.DataFrame(list(country_against.items()),columns = ['Country','Goals Against']) 

df_country_against_sorted = df_country_against.sort_values(by = "Goals Against", ascending = True)

#%%- q7 [ ] en uzun yenilmezlik unvani

time1 = time.time()
country_win_streak ={}


for row in df_scores_imp.itertuples():
    
    if row.home_team not in country_win_streak:
        country_win_streak[row.home_team] = []
    if row.away_team not in country_win_streak:
        country_win_streak[row.away_team] = []
        
    if row.home_ft > row.away_ft:
        country_win_streak[row.home_team].append("W")
        country_win_streak[row.away_team].append("L")
    elif row.home_ft < row.away_ft:
        country_win_streak[row.home_team].append("L")
        country_win_streak[row.away_team].append("W")
    elif row.home_ft == row.away_ft:
        country_win_streak[row.home_team].append("D")
        country_win_streak[row.away_team].append("D")

df_country_win_streak = pd.DataFrame(list(country_win_streak.items()),columns = ['Country','Win_Streak']) 


streaks = []

for row in df_country_win_streak.itertuples():
    win_streak = 0
    max_streak = 0

    for match in row.Win_Streak:
        if match == "W":
            win_streak+=1
        elif match == "L" or match == "D":
            if win_streak > max_streak:
                max_streak = win_streak
            win_streak = 0
    streaks.append(max_streak)     


df_country_win_streak.Win_Streak = streaks
    
df_country_win_streak_sorted = df_country_win_streak.sort_values(by = "Win_Streak", ascending = False)
    
time2 = time.time()

time_dif = time1 - time2
#%% - q8 [ ] her turnuva tipindeki mac sayisi

ser_tournament_count = df_scores["tournament"].value_counts()



#%% sample

df_sample_1 = df_scores.sample(20,random_state = 9)

















