#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:45:08 2019

@author: sandeep
"""

def func(a,b,c):
    if c == True:
        return a
    else:
        return b
    
    
d = bool(input())
print(func('Hello','Goodbye',d))