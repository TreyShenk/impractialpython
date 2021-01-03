#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
All Anagram Finder
This anagram will list all of the possible anagrams for an input. This was 
inspired by Lee Vaughan's "Impractical Python" which does the same thing in a
more user-directed way. Vaughan lets the user pick the anagram one word at a 
time. This is more likely to produce an interesting anagram, but it is also 
easy to get stuck.
The biggest coding difference is that the program had to semi-efficiently go 
through every possible combination. I decided to achieve this by using a tree
structure, so that the steps after deciding an input would be
    1. Find all of the words that can be made using the current letters.
    2. For each word, remove the "word" letters and repeat with remaining 
       letters.
This process builds up an anagram tree.

One important design choice was that the dictionary for step 2 only includes 
the chosen word and the words following. Means ensures that no two branches 
will have the same words in different order. If this were not the case, the 
number of possibilities would be much larger.
        
@author: Trey E. Shenk
"""
import load_dictionary as ld
from collections import Counter

# This corncob list, which is Mieliestronk's list of Enlish words, is good if
# you want lots of options. For this current project, it produces too many 
# spurious phrases. You can see that I tried paring the list down before 
# deciding to use a much shorter dictionary file.
# dict_list = ld.load('corncob_lowercase.txt')
# to_remove = ['eh', 'ne', 'em', 're', 'ems', 'els', 'abe',
#              'aden','ben','sen','ibsen']
# for word in to_remove:
#     dict_list.remove(word)


dict_list = ld.load('common_words.txt')
# Make sure that "I" and "a" are included as they are useful in anagrams.
to_append = ['i', 'a']
for word in to_append:
    if word not in dict_list:
        dict_list.append(word)
# It is important to sort the list after appending the words.
dict_list = sorted(dict_list)

# This definition of the anagram tree structure is the key part of the code
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
        # Finds all possible words that can be made with the remaining
        # letters and adds them as children of the current node. Note that 
        # after the children are found, they are all added, then each child is
        # looped through to find its own children.
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
                    # If a child has no remaining letters, then it was a 
                    # successful branch. It will be printed when found and
                    # also store for later use (if later use is desired).
                    child.print_anagram()
                    child.store_anagram('')
        else:
            # If there are no possible anagrams from the remaining letters, 
            # then this branch was unsuccessul and needs to be pruned.
            self.parent.delete_branch(self)
    
    def delete_branch(self, child):
        # A key point here is knowing how far to prune back.
        if len(self.children)==1 and self.tree_level>0:
            # If branch to delete is an only-child, then the parent should
            # also be deleted.
            self.parent.delete_branch(self)
        else:
            self.children.remove(child)
            #print("Delete on level {}, word is {}, remaining {}".format(child.tree_level, child.word, child.remaining))
    
    def store_anagram(self, current_phrase):
        # When a successful anagram is found, this builds the phrase from the 
        # leaf to the root, and stores the result in the root node.
        if self.tree_level>0:
            current_phrase = current_phrase +' '+ self.word
            self.parent.store_anagram(current_phrase)
        else:
            self.anagram_list.append(current_phrase)
    
    def print_anagram(self):
        # This prints the anagram from tree to root.
        print(self.word, end=" ")
        if self.tree_level>1:
            self.parent.print_anagram()
        else:
            print()
            
    def add_child(self, word):
        # Add a new child node using one of the possible words.
        remaining_letters = list(self.remaining)
        for letter in word:
            remaining_letters.remove(letter)
        child = AnagramTree(''.join(remaining_letters))
        child.word = word
        child.parent = self
        child.tree_level = self.tree_level+1
        # dict_ind is used for further anagram lookups. By only using the words
        # after and including the current word, we have greatly reduced the 
        # search space and size of the resulting tree.
        child.dict_ind = dict_list.index(word)
        self.children.append(child)

    def print_tree(self):
        # This will print the tree in a somewhat readable tree structrue.
        prefix = ' '*2*self.tree_level+'|__' if self.parent else ''
        print(prefix + self.word)
        for child in self.children:
            child.print_tree()


def find_anagram(possible_letters, word_list):
    # This function is taken from Impractical Python. It finds the possible 
    # single words that can be made using a set of letters.
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
    ini_name = input('Input a name to find anagrams: ')
    # Convert to lower case and remove spaces
    ini_name = ''.join([i.lower() for i in ini_name if i.isalpha()])
    at = AnagramTree(ini_name)
    at.find_children()
    at.print_tree()
    return at
if __name__=='__main__':
    main()
    
    
    
    