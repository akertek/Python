#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 16:10:04 2020

@author: egeakertek
"""
import re

# dosyadan elemanları teker teker çekmek için kullandım.
def only_words(my_string):
    """ returns all the words inside a sentence"""
    words = re.findall(r'\w+', my_string)
    return words
dummy = []
standings = {}
new_lines = []

# Dosyayı okudum.
handle = open("maçlar.txt", "r", encoding="utf8")
lines = handle.readlines()
handle.close()

#Boşlukları sildim.
new_lines = [x for x in lines if x.strip()]

# Tüm satırların başındaki ve sonundaki boşlukları attım.
for line in new_lines:
    dummy.append(only_words(line.strip()))

#Takımlara ve skorlara eriştim.
for element in dummy:
    team1 = element[0]
    score1 = element[1]
    team2 = element[3]
    score2 = element[2]
#Puan eklemelerini yaptım.
    if team1 not in standings:
        standings[team1] = 0
    if team2 not in standings:
        standings[team2] = 0

    if score1 > score2:
        standings[team1] += 3
    elif score1 < score2:
        standings[team2] += 3
    else:
        standings[team1] += 1
        standings[team2] += 1

# Puan durumuna göre sıraladım.
standings = sorted(standings.items(), key=lambda x: x[1], reverse=True)

#Voila!
for each_team in standings:
    print(each_team[0], "-- ", each_team[1])
