#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 11:51:39 2020

@author: egeakertek
"""
from math import sqrt
# Roots of a Quadratic Equation


def find_roots(num_a, num_b, num_c):
    """Roots of a Quadratic Equation"""
    discriminant = num_b**2 - 4*num_a*num_c

    if discriminant < 0:

        print("There are no real roots. Discriminant is < 0")


    elif discriminant == 0:

        root = (-num_b)/2*num_a
        print("There is one root: ", root)


    elif discriminant > 0:
        root1 = (((-num_b) + sqrt(discriminant))/(2*num_a))
        root2 = (((-num_b) - sqrt(discriminant))/(2*num_a))
        print("There are two roots: %f and %f" % (root1, root2))


find_roots(5, 4, 5)
