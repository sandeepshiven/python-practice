#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 13:08:47 2019

@author: sandeep
"""

def prime(num):
    for i in range(2,num-1):
        if num%i == 0:
            return "Not a Prime number"
    return "Prime number"

number = int(input("Enter a number\n"))
print(prime(number))