#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 22:17:30 2019

@author: sandeep
"""

d = {'k1':1,'k2':2,'k3':3}

for item in d:
    print(item) # this will print keys

for keys in d.values(): # now this will print values
    print(keys)

print(d.items())

# dictionary unpacking
for k,v in d.items():
    print(k)
    print(v)



