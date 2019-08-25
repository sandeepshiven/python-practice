# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 16:41:16 2019

@author: sande
"""

from collections import defaultdict

d = {'k1' : 1}

print(d['k1'])

try:
    print(d['k2'])  # this will raise a key error
except:
    print("KeyError: 'k2'")
    
    
d = defaultdict(object) # A defaultdict will never raise a KeyError. Any key that does not exist gets the value returned by the default factory.

print(d['k2']) # returns the object location


for i in d:
    print(i)
    
d = defaultdict(lambda:0) # initializing with default value


print('\n\n\n',d['k2'])








