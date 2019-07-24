#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 17:02:25 2019

@author: sandeep
"""

st = 'Print only the words that start with s in this sentence'

for word in st.split():
    if word[0] == 's':
        print(f"{word} ")
        