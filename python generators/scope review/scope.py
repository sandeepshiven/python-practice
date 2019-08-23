#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 12:07:09 2019

@author: sandeep
"""

the_global = "My Global Variable"

def my_function():
    ''' checking for
    local vairable'''
    the_local = "My Local Variable "
    print(locals()) # prints the local variables inside the function
    
print(globals())  # prints dictionary of all global variables

print('\n\n',globals().keys()) # prints keys of all global variables

print('\n\n\n',globals()['the_global'],'\n\n\n') # garbs the key and prints value assigned to it







my_function()













