#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 17:47:22 2019

@author: sandeep
"""

st = 'Create a list of the first letters of every word in this string'

lst = [x[0] for x in st.split() ]
print(lst)