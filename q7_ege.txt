#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 10:33:56 2020

@author: egeakertek
"""

def is_it_sorted(my_list):
    """ listenin sıralı mı değil mi olduğunu döndüren fonksiyon"""

    buffer = my_list.copy()
    buffer.sort()

    return buffer == my_list

test = is_it_sorted([1, 2, 3, 4])
