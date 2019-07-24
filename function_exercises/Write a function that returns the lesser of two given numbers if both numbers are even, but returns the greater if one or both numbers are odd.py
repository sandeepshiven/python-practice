#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 19:31:36 2019

@author: sandeep
"""

def lesser_of_two_evens(a,b):
    if a%2 ==0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)

# Check
print(lesser_of_two_evens(2,4))

# Check
print(lesser_of_two_evens(2,5))



