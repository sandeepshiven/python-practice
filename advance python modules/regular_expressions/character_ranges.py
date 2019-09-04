#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:09:12 2019

@author: sandeep
"""




import re

def multi_re_find(patterns,phrase):
    for pattern in patterns:
        print(f"Searching the phrase using the re check: {pattern}")
        print(re.findall(pattern,phrase))
        print('\n')


test_phrase = 'This is an example sentence. Lets see if wecan find some letters.'

test_patterns = ['[a-z]+', # sequence of lower case words
                 '[A-Z]+', # sequence of upper case letters
                 '[a-zA-z]+', # sequence of lower or upper case letters
                 '[A-Z][a-z]+' # one upper case letter followed by lower case letters
                 ]

multi_re_find(test_patterns,test_phrase)












