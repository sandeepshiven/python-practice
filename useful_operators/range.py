#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 22:41:40 2019

@author: sandeep
"""

print(f"{list(range(0,10,2))}")  # can be created as list or tuples by casting

# syntax of range: range(start,stop,step)

# use of range in for loop

list1 = [2,3,4,67,8,9,0,34,54,57]

for list2 in range(10):
    if list1[list2] in range(20):
        print(f"{list1[list2]}")
    


# range is a generator it means it just genrates data does not stores data in memory




