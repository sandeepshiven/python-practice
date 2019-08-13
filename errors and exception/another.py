#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 15:16:40 2019

@author: sandeep
"""

# using try except for prompting user for entering the correct input
def ask_for_int():
    
    while True:
        try:
            result = int(input("Please enter a number: "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("Yes thank you")
            break
            # not using finally because it runs no matter what
            # it is good if you want to do some additional operation
            
            
ask_for_int()