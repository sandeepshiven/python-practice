#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 21:54:24 2019

@author: sandeep
"""

def spy_game(nums):
    code = [0,0,7,'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

print(spy_game([1,2,4,0,0,7,5]))

# Check
print(spy_game([1,0,2,4,0,5,7]))

# Check
print(spy_game([1,7,2,0,4,5,0]))