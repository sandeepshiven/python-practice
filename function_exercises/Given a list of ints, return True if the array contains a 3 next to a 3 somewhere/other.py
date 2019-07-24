#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 20:08:00 2019

@author: sandeep
"""

def has_33(num):
    for i in range(0,len(num)-1):
        if num[i:i+2] == [3,3]:
            return True
    return False
# Check
print(has_33([1, 3, 3]))

# Check
print(has_33([1, 3, 1, 3]))

# Check
print(has_33([3, 1, 3]))
