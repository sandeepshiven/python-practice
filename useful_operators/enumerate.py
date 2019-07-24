#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 23:09:57 2019

@author: sandeep
"""

string = 'Sandeep'

print(f"{dict(enumerate(string))}")

print(f"{tuple(enumerate(string))}") 

print(f"{list(enumerate(string))}")

# enumerate just pairs up the string elements by indexing


item_count = 0
for item in string:
    print(f"{item} is at index {item_count}")
    item_count += 1
    
print("\n\n")

# now we can do this with eleminating the extra varaiable by using enumerate

for index,value in enumerate(string):
    print(f"{value} is at index {index}")




