#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 12:54:54 2020

@author: egeakertek
"""

def is_prime(num):
    """ Finding if a number is pirme or not."""
    num_found = False
    if num > 1:
        for i in range(2, num//2 + 1):
            if (num % i) == 0:
                num_found = False
                break
            else:
                num_found = True

    else:
        num_found = False
    return num_found

state = is_prime(33)

def next_prime(num):
    """ Finding the next prime number"""
    num += 1
    while is_prime(num) is False:
        num += 1
    return num

next_num = next_prime(5)
