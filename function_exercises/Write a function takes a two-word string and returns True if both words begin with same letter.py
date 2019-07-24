#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 19:33:32 2019

@author: sandeep
"""

def animal_crackers(text):
    string = list(text.split())
    return string[0][0] == string[1][0]

# Check
print(animal_crackers('Levelheaded Llama'))

# Check
print(animal_crackers('Crazy Kangaroo'))