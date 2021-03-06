#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 09:37:00 2020

@author: egeakertek
"""
def tc_kimlik_sorgula(kimlik_no):
    """ TC Kimlik Doğrulama Algoritması"""

    sum1 = 0
    sum2 = 0
    sum3 = 0

    for i in range(0, 9, 2):
        print(i)
        sum1 += int(kimlik_no[i])
    print(sum1)
    for i in range(1, 8, 2):
        print(i)
        sum2 += int(kimlik_no[i])
    print(sum2)
    for i in range(0, 10, 1):
        print(i)
        sum3 += int(kimlik_no[i])

    print(sum3)
    rule_0 = kimlik_no[0]
    rule1 = (sum1*7 - sum2)%10
    rule2 = sum3%10

    if rule_0 == 0:
        return False
    elif rule1 is not int(kimlik_no[9]):
        return False
    elif rule2 is not int(kimlik_no[10]):
        return False
    else:
        return True

is_correct = tc_kimlik_sorgula('29308128070')
