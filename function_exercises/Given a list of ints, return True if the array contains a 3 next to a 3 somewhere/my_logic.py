#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 20:05:53 2019

@author: sandeep
"""

def has_33(nums):
    for i in  range(len(nums)-1):
        if (nums[i]==3) and (nums[i+1] == 3):
            return True
        
    return False
# Check
print(has_33([1, 3, 3]))

# Check
print(has_33([1, 3, 1, 3]))

# Check
print(has_33([3, 1, 3]))