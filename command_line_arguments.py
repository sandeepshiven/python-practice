#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 12:00:28 2019

@author: sandeep
"""

import sys

num = sys.argv[1]
file = sys.argv[0]

print("I am running the {} file".format(file))

y=[ x for x in range(int(num)) if x%2 == 0]
print(f"{y}")