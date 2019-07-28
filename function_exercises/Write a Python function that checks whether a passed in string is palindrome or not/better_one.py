#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 19:56:24 2019

@author: sandeep
"""

def palindrome(s):
    s = s.replace(" ",'') # This replaces all spaces ' ' with no space ''. (Fixes issues with strings that have spaces)
    return s == s[::-1]

print(palindrome('nurses run'))