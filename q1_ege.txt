#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 11:21:29 2020

@author: egeakertek
"""

# Primary Solution


grid = 'E3'
grid = grid.strip()

letter = grid[0].capitalize()
number = int(grid[1])s

alpha = ['A', 'C', 'E', 'G']

if number%2 == 0:        # If it is even then letters in alpha will be white.
    if letter in alpha:
        print("White!")
    else:
        print("Black!")
else:                    # If it is odd it is the opposite thing. 
    if letter in alpha:
        print("Black!")
    else:
        print("White!")




#%%

# Secondary Solution

grid = '6e'.strip().capitalize()

blacks = ['A1', 'C1', 'E1', 'G1', '2B', '2D', '2F', '2H', '3A', '3C',
          '3E', '3G', '4B', '4D', '4F', '4H', '5A', '5C', '5E', '5G',
          '6B', '6D', '6F', '6H', '7A', '7C', '7E', '7G', '8B', '8D',
          '8F', '8H']

if grid in blacks:
    print("Black!")
else:
    print("White!")
