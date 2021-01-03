#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:23:38 2021

@author: trey
"""
import load_dictionary as ld
from collections import Counter

dict_list = ld.load('corncob_lowercase.txt')

to_remove = ['eh', 'ne', 'em', 're', 'ems', 'els', 'abe',
             'aden','ben','sen','ibsen']
for word in to_remove:
    dict_list.remove(word)
    
dict_list = ld.load('common_words.txt')
to_append = ['i', 'a']
for word in to_append:
    if word not in dict_list:
        dict_list.append(word)
dict_list = sorted(dict_list)
class AnagramTree:
    def  __init__(self, remaining):
        self.word = ''
        self.remaining = remaining
        self.parent = None
        self.children = []
        self.tree_level = 0
        self.dict_ind = 0
        self.anagram_list = []
    
    def find_children(self):
        #self.print_tree()
        this_word_list = dict_list[self.dict_ind::]
        anagram_list = find_anagram(self.remaining, this_word_list)
        if anagram_list:
            #print('Level: {}, new nodes: {}'.format(self.tree_level+1, len(anagram_list)))
            for word in anagram_list:
                self.add_child(word)
            for child in self.children[:]:
                if child.remaining:
                    child.find_children()
                else:
                    child.print_anagram()
                    child.store_anagram('')
        else:
            self.parent.delete_branch(self)
    
    def delete_branch(self, child):
        if len(self.children)==1 and self.tree_level>0:
            self.parent.delete_branch(self)
        else:
            self.children.remove(child)
            #print("Delete on level {}, word is {}, remaining {}".format(child.tree_level, child.word, child.remaining))
    def store_anagram(self, current_phrase):
        if self.tree_level>0:
            current_phrase = current_phrase +' '+ self.word
            self.parent.store_anagram(current_phrase)
        else:
            self.anagram_list.append(current_phrase)
    def print_anagram(self):
        print(self.word, end=" ")
        if self.tree_level>1:
            self.parent.print_anagram()
        else:
            print()
            
    def add_child(self, word):
        remaining_letters = list(self.remaining)
        for letter in word:
            remaining_letters.remove(letter)
        child = AnagramTree(''.join(remaining_letters))
        child.word = word
        child.parent = self
        child.tree_level = self.tree_level+1
        child.dict_ind = dict_list.index(word)
        self.children.append(child)

    def print_tree(self):
        prefix = ' '*2*self.tree_level+'|__' if self.parent else ''
        print(prefix + self.word)
        for child in self.children:
            child.print_tree()

def find_anagram(possible_letters, word_list):
    possible_letters_map = Counter(possible_letters)
    anagrams = []
    for word in word_list:
        test=''
        word_letter_map = Counter(word.lower())
        for letter in word:
            if word_letter_map[letter]<=possible_letters_map[letter]:
                test += letter
        if Counter(test) == word_letter_map:
            anagrams.append(word)
    return anagrams

def main():
    anagram_phrases = []
    ini_name = input('Input a name to find anagrams: ')
    # Convert to lower case and remove spaces
    ini_name = ''.join([i.lower() for i in ini_name if i.isalpha()])
    at = AnagramTree(ini_name)
    at.find_children()
    at.print_tree()
    return at
if __name__=='__main__':
    main()
    
    
    
    