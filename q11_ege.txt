#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 14:46:24 2020

@author: egeakertek
"""
import re


def only_words(my_string):
    """ returns all the words inside a sentence"""
    
    words = re.findall(r'\w+', my_string.strip())
    return words

words = only_words("Examples of contractions include: don’t, isn’t, and wouldn’t.")
