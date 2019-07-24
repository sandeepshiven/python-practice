#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 23:08:53 2019

@author: sandeep
"""

def is_greater(a,b):
    return a>b

num1,num2 = input("Enter two mumbers\n").split() # method for taking multiple input

print(f"Is {num1} greater than {num2}\n{is_greater(num1,num2)}")

num1,num2 = [input() for i in range(2) ]

print(f"Is {num1} greater than {num2}\n",is_greater(num1,num2))
















