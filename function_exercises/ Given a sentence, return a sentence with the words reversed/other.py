#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 19:59:52 2019

@author: sandeep
"""

def master_yoda(text):
    return ' '.join(text.split()[::-1])
# Check
print(master_yoda('I am home'))

# Check
print(master_yoda('We are ready'))