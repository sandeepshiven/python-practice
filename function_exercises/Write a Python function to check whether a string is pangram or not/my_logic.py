#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 20:01:10 2019

@author: sandeep
"""

import string

def ispangram(str1, alphabet=string.ascii_lowercase): # long and buggy method but works fine
    num = 0
    alphabet1 = [i for i in alphabet] # no need to do this
   # print(alphabet1)
    str2 = list(set([i for i in str1.lower()])) # this too is unneccesary
    for item in alphabet1:
        if item in str2:
            num +=1
        else:
            continue
    return num == 26


print(ispangram("The quick brown fox jumps over the lazy dog"))