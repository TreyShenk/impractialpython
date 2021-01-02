#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Single word anagram finder.

@author: trey
"""
import load_dictionary as ld


def main():
    # Load the dictionary file
    word_list = ld.load('corncob_lowercase.txt')
    
    # Accept a word from the user
    user_word = input("\nInput a word to find the anagrams: ")
    # Sort the user-word
    user_word_srt = sorted(user_word)
    
    # Create an empty list to hold the anagrams
    anagrams_list = []
    # Loop through each word in the word list
    for check_word in word_list[:]:
        # Sort the word
        check_word_srt = sorted(check_word)
        
        # Check to see if sorted word is equal to the sorted user-word 
        if check_word_srt == user_word_srt and check_word != user_word:
            # Append to list of anagrams
            anagrams_list.append(check_word)
    
    # Print list of anagrams
    print(anagrams_list)
    
if __name__ == "__main__":
    main()