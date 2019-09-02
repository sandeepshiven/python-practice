#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 00:01:30 2019

@author: sandeep
"""

import timeit


#for loop
print(timeit.timeit('"-".join(str(i) for i in range(1000))',number = 10000))

#list comprehension
print(timeit.timeit('"-".join([str(i) for i in range(1000)])',number = 10000))

#map
print(timeit.timeit('"-".join(map(str,range(1000)))',number = 10000))

