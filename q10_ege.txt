#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 13:21:35 2020

@author: egeakertek
"""

def is_perfect_number(my_num):
    """ Verilen sayı perfect mi değil mi olnu bulan fonksiyon"""

    divisors = []

    for number in range(1, my_num//2 + 1):
        if my_num % number == 0:
            divisors.append(number)

    total = sum(divisors)

    return total == my_num

perfect_number = is_perfect_number(28)
