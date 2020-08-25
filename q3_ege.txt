#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 12:09:14 2020

@author: egeakertek
"""

#Pi Number Calculation

def pi_approx(approx_num):
    """ Pi Number Approximation with given number."""
    pi_calc = 3
    num = 1
    dummy = 2
    sign = 1
    while num <= approx_num:

        print(round(pi_calc, 15))
        pi_calc += sign*(4/ (dummy*(dummy+1)*(dummy+2)))
        sign = sign*(-1)
        dummy += 2
        num += 1



pi_approx(15)
