#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 09:32:05 2020

@author: trey
"""

import load_dictionary as ld
word_list = ld.load('words_alpha.txt')
pali_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

print("\nNumber of panlindromes found = {}\n".format(len(pali_list)))
print(*pali_list, sep='\n')