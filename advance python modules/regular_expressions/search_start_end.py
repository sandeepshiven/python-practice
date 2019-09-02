#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 23:59:41 2019

@author: sandeep
"""


import re

patterns = ['term1','term2'] #List of patterns to search for

text = "This is a string with term1, but not the other one"

for pattern in patterns:
    print(f"Searching for {pattern} in:\n{text}\n")
    
    if re.search(pattern,text):
        print("Match found\n")
    else:
        print("Match not found\n")
 
pattern = 'term1'       
match = re.search(pattern,text) # returns a match object

print(type(match))


'''
This Match object returned by the search() method is more than just a Boolean or None, 
it contains information about the match, including the original input string, the regular
 expression that was used, and the location of the match. 
'''
print(match.start()) # location of the match that was found

print(match.end()) # location at which the match ends















