#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 20:03:32 2019

@author: sandeep
"""
def almost_there(n):
    return abs(n-100) <= 10  or abs(n-200) <= 10

# Check
print(almost_there(90))

# Check
print(almost_there(150))

# Check
print(almost_there(209))
