#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 14:24:28 2019

@author: sandeep
"""

def ran_check(num,low,high):
    if num >= low or num <= high: # can use range function also
        print(f"{num} is in the range between {low} and {high}")
    else:
        print(f"{num} is not the range between {low} and {high}")
        

# Check
print(ran_check(5,2,7))

# below function returns boolean value
def ran_bool(num,low,high):
    return ((num >= low) or (num<= high)) # can use range function also

print(ran_bool(3,1,10))