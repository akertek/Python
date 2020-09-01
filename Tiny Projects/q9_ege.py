#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 12:51:57 2020

@author: egeakertek
"""

def remove_outliers(data_list, allowed_range):
    """Verilen bir aralık dışındaki elemanlari çıkaran bir fonksiyon"""
    begin = allowed_range[0]
    end = allowed_range[1]

    try:
        begin_index = data_list.index(begin)
    except ValueError as error:
        print(f'Element "{begin_index}" not found in the list: ', error)
    try:
        end_index = data_list.index(end)
    except ValueError as error:
        print(f'Element "{end_index}" not found in the list: ', error)

    return data_list[begin_index:end_index + 1]

new_list = remove_outliers([1, 2, 3, 4, 5, 6], [2, 4])
