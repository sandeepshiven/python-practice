#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 22:02:32 2019

@author: sandeep
"""

def fib(n):
    a =1
    b = 1
    for i in range(n):
        yield a
        a,b = b,b+a
        
for i in fib(10):
    print(i)















