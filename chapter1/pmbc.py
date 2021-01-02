#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Poor Man's Bar Chart

Created on Sat Dec 12 19:25:17 2020


@author: Trey E. Shenk
"""
import pprint
from collections import defaultdict


def main():
    histogram = defaultdict(list)
    
    # Read in a string and strip off any characters that are not alphabetic.
    input_string = input("Input a string, and this will output a histogram.\n")
    input_string = [i for i in input_string if i.isalpha()]
    
    # Make a dictionary, using the characeter as the key. If the key already 
    # exists, put another character in the field. 
    for character in input_string[:]:
        if character in histogram:
            histogram[character] = histogram[character]+character
        else:
            histogram[character] = character
    
    # Use prettyprint to make the output more human-readable.
    pprint.pprint(histogram)
                
if __name__ == "__main__":
    main()
