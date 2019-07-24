#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 19:51:51 2019

@author: sandeep
"""

def master_yoda(text):
    original = list(text.split())
    reverse = []
    for i in range(len(original)-1,-1,-1):  # the logic in range function is used to give list of reversed numbers upto 0
        #print(original)
        reverse.append(original[i]) 
    return ' '.join(reverse)

# Check
print(master_yoda('I am home'))

# Check
print(master_yoda('We are ready'))
