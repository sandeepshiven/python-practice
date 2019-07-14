#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 15:25:35 2019

@author: sandeep
"""

def fact(n):
    if n >= 1:
        return (n * fact(n-1))
    else: 
        return 1
        
    
print(f" The factorial of 4 is {fact(4)}")