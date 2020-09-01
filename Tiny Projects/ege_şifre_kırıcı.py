#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 18:25:19 2020

@author: egeakertek
"""

import re
import operator
import string

def word_count(my_str):
    """#function for finding most frequent words. Output will be filled with tuples."""
    counts = dict()
    words = re.findall(r'\w+', my_str.strip())

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    sorted_words = sorted(counts.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_words

def find_max_letter_count(text):
    """function for letter frequency."""
    alphabet = string.ascii_lowercase
    letter_freq = {}

    for letters in alphabet:
        letter_freq[letters] = 0

    for letters in text:
        try:
            letter_freq[letters] += 1
        except KeyError:
            continue

    letter_freq = sorted(letter_freq.items(), reverse=True, key=lambda x: x[1])

    return letter_freq


def decryption_machine(text, decryption):
    """function for letter frequency."""
    dec_text = []
    for letter in text:
        try:
            dec_text.append(decryption[letter])
        except KeyError:
            dec_text.append('*')
        dect_text_str = ''.join(dec_text)
    return dect_text_str

def mother_decryption_machine(file):
    """Bigger decryption function"""
    #File Operations
    handle = open(file, "r", encoding="utf8")
    text = handle.read()
    handle.close()

    #Most frequent word and letter are found.
    word_freq = word_count(text)
    letter_freq = find_max_letter_count(text)

    #Created a dict. for decryption.
    decryption = {}
    punc = string.punctuation

    #Punctuations are added.
    for each_punc in punc:
        decryption[each_punc] = each_punc

    #This is the decryption codes I found with brute force."
    decryption['/n'] = ''
    decryption[' '] = ' '
    decryption['m'] = 't' #mfn
    decryption['f'] = 'h' #mfn
    decryption['n'] = 'e'
    decryption['k'] = 'a'
    decryption['q'] = 'n'
    decryption['r'] = 'd'
    decryption['z'] = 'o'
    decryption['o'] = 'i'
    decryption['e'] = 's'
    decryption['u'] = 'w'
    decryption['y'] = 'g'
    decryption['j'] = 'r'
    decryption['i'] = 'u'
    decryption['p'] = 'b'
    decryption['w'] = 'l'
    decryption['l'] = 'm'
    decryption['s'] = 'c'
    decryption['a'] = 'f'
    decryption['g'] = 'k'
    decryption['t'] = 'y'
    decryption['h'] = 'z'
    decryption['d'] = 'p'
    decryption['c'] = 'v'
    decryption['x'] = 'x'
    decryption['b'] = 'j'
    decryption['v'] = 'q'

    #All decrypted words. I checked regularly this list with word_freq. 
    #That's how I found decryption.
    decrpyted_words = []

    for num in range(0, len(word_freq)):
        decrpyted_words.append(decryption_machine(word_freq[num][0], decryption))

    decrypted_text = decryption_machine(text, decryption)

    return decrpyted_words, decrypted_text

last_decrpyted_words, last_decrypted_text = mother_decryption_machine("crypted.txt")
