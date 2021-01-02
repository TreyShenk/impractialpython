#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 11:36:45 2020

@author: trey
"""

def ispalindrome(test_word):
    if len(test_word)==1 or len(test_word)==0:
        return True
    elif test_word[0]==test_word[-1]:
        return ispalindrome(test_word[1:-1])
    else:
        return False


def main():
    import load_dictionary as ld
    word_list = ld.load('common_words.txt')
    
    # Define a minimum baseword length to produce more interesting results
    min_base_len = 2
    test_list = [i for i in word_list if len(i)>=min_base_len]
    pali_list = []
    word_list = set(word_list)
    for tmp_word in test_list[:]:
        end = len(tmp_word)
        #rev_word = tmp_word[::-1]
        for i in range(end):
            if tmp_word[i::-1] in word_list and ispalindrome(tmp_word[(i+1):]):
                pali_list.append(tmp_word+' '+tmp_word[i::-1])
                print(pali_list[-1])
            if tmp_word[-1:-(2+i):-1] in word_list and ispalindrome(tmp_word[:-(i+1)]):
                pali_list.append(tmp_word[-1:-(2+i):-1]+' '+tmp_word)
                print(pali_list[-1])
    
    print("There were {} word-pair palingrams found!".format(len(pali_list)))

if __name__ == "__main__":
    main()