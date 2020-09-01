#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 13:57:42 2020

@author: egeakertek
"""
import random

alphabet = ['A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'Y', 'Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


two_or_three = random.randint(0, 1)


if two_or_three:
    plate = str(random.randint(1, 82)) +' '+ ''.join(random.sample(alphabet, 2)) +' ' + str(random.randint(100, 1000))
else:
    plate = str(random.randint(1, 82)) +' '+ ''.join(random.sample(alphabet, 3)) +' ' + str(random.randint(10, 100))
