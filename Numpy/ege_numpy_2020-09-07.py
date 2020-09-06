#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 12:47:22 2020

@author: egeakertek
"""

import numpy as np


#%%
# q1: Sadece boolean False degerinden olusan, 5x5 boyutunda bir ndarray oluşturunuz.

boolean_array = np.full((5, 5), False)


#%%
# q2: 1'den 1000'e kadar olan tam sayılardan oluşan bir ndarray oluşturunuz
# bunun içinden 42'ye tam bölunebilen sayıları secip, ayrı bir ndarray'de toplayınız.

my_array_2 = np.arange(1, 1001)

array_42 = my_array_2[my_array_2 % 42 == 0]

#%%

# q3: bir ndarray içinden, en küçük ve en büyük değerleri secen bir kod yazınız.

def big_and_small(my_arr):
    return my_arr.max(0), my_arr.min(0)

test_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

maximum, minimum = big_and_small(test_arr)

#%%

# q4: bir ndarray içinden, en büyük 3 sayıyı secen bir kod yazınız.


def big_three(my_arr):

    temp_arr = np.partition(-my_arr, 3)[:3]
    result = -temp_arr[:3]

    return result

test_arr = np.arange(1, 100001)

big_three_arr = big_three(test_arr)

#%%

# q5: [0, 1, 0, 1...] (toplam uzunluğu 40) olacak şekilde bir ndarray oluşturunuz.

repeated_arr = np.tile([0, 1], 20)

#%%

# q6: bir ndarray'i reverse ediniz.

test_arr = np.arange(1, 101)

flipped_arr = test_arr[::-1]

#%%

# q7: 7x7 uzunlugunda bir birim matris oluşturunuz.

identity_matrix = np.identity(7, dtype = int)

#%%

# q8: Kenarlarında 1, ortasında 0 olan, 10x10 bir matris oluşturunuz.

weird_arr = np.full((10, 10), 1)

weird_arr[1:9, 1:9] = 0

#%%

# q9: Siyah kareler için 1, beyaz kareler için 0 olacak şekilde, bir satranç tahtasını temsil eden bir matris oluşturunuz.

tile_arr = np.array([(0, 1), (1, 0)])

chess_board = np.tile(tile_arr, (4, 4))

#%%

# q10: 10x10 boyutunda, 0 ile 100 (dahil) arasında float sayılardan oluşan bir matris yaratınız.

my_arr10 = np.random.uniform(1.0, 101.0, (10, 10))

#%%

# q11: q10'daki matris'deki her sayıyı, taban değerine yuvarlayınız.


my_arr10 = np.random.uniform(1.0, 101.0, (10, 10))

floored_arr = np.floor(my_arr10)

#%%

# q12: 5x5 boyutunda 2 adet ndarray'in, birbirine eşit olup olmadığını bulunuz.

def is_equal(arr1, arr2):

    return (arr1 == arr2).all()

my_arr1 = np.full((5, 5), 1)
my_arr2 = np.full((5, 5), 2)

equality_check = is_equal(my_arr1, my_arr2)

#%%

# q13: 5x5 boyutunda bir ndarray olsun. 5x5=25 hücrenin ortalamasını alıp, 5x5 hücrenin en ortasındaki hücreye yazdırınız.

my_arr2 = np.random.uniform(11.0, 100.0, (5, 5))

mean_value = my_arr2.mean()

my_arr2[2][2] = mean_value

