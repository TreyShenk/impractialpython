#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:23:38 2021

@author: trey
"""
import load_dictionary as ld
from collections import Counter
dict_list = ld.load('corncob_lowercase.txt')

def find_anagram(full_word_map, word_list):
    anagrams_found = []
    
    # If the test word does not fit, return an empty list
    
    # If the test word does fit, add it to the current list, and try again
    # with the remaining letters
    
    # If the test word does fit, and there are no remaining letters, return
    # the current list and mark as finished
    
    
    
def main():
    ini_name = 'Donald John Trump'
    # Convert to lower case and remove spaces
    ini_name = ''.join([i.lower() for i in ini_name if i.isalpha()])
    word_list = dict_list;
    