#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 14:29:23 2019

@author: sandeep
"""

try:
    
    # want to attempt this code
    # may have an error
    result = 10 + '10'
    
except:
    print("Hey! looks like you are not adding correctly")
    
try:
    
    # want to attempt this code
    # may have an error
    result = 10 + 10
    
except :  # runs only if there is an error
    print("Hey! looks like you are not adding correctly")
    
else: # if there is no error this will run
    print("Addition went well")
    print(result)



    