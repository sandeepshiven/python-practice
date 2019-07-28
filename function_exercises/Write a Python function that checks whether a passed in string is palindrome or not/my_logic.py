#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 19:55:01 2019

@author: sandeep
"""

def palindrome(s): # this method does not removes and checks special characters and spaces 
    string = s[::-1]
    return string == s

print(palindrome('helleh'))
print(palindrome('nurses run')) # this is also a palindrome but due to whitespace program is not delivering desired result

