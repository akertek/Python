#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 12:18:05 2020

@author: egeakertek
"""

def insert_element(element, my_list):
    """ Doğru konuma element insertleyen bir fonksiyon"""
    insert_index = 0
    for list_element in my_list:
        if element > list_element:
            insert_index += 1
    my_list.insert(insert_index, element)


test_list = [1, 2, 3, 4, 6]
insert_element(5, test_list)
