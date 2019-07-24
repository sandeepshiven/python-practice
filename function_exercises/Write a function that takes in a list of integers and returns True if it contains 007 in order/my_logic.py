#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 21:52:11 2019

@author: sandeep
"""

def spy_game(nums):
    bond = []
    for item in nums:
        if item == 0 or item == 7:
            bond.append(item)
    return bond == [0,0,7]
# Check
print(spy_game([1,2,4,0,0,7,5]))

# Check
print(spy_game([1,0,2,4,0,5,7]))

# Check
print(spy_game([1,7,2,0,4,5,0]))