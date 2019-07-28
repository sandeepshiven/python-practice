#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 19:54:14 2019

@author: sandeep
"""

def multiply(numbers):  
    y=1
    for i in numbers:
        y *= i
    return y

print(multiply([1,2,3,-4]))