#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:41:51 2019

@author: sandeep
"""
import re




def multi_re_find(patterns,phrase):
    ''' 
    Takes a list of patterns
    prints a list of all matches
    '''
    for pattern in patterns:
        print(f"Searching the phrase using the re check: {pattern}")
        print(re.findall(pattern,phrase))
        print('\n')
        
test_phrase = 'sdsd..sssddd...sdddsddd...dsdds...dsssss...sdddd'

test_patterns = ['sd*',  # s followed by zero or more d's
                 'sd+',  # s followed by one or more d's
                 'sd?',  # s followed by zero or one d's 
                 'sd{3}', # s followed by three d's
                 'sd{2,3}', # s followed by two to three d's
                 # character sets
                 '[sd]', # searches for either s or d
                 's[sd]+' # s followed by one or more s or d
                 
                 ]

multi_re_find(test_patterns,test_phrase)














