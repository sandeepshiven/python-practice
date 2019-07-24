#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 16:43:48 2019

@author: sandeep
"""

# we use **kwargs to handle arbitrary numbers of keyworded arguments

# **variable builds a dictionary of ket value pairs

def foo(**kwargs):
    print(f"The fruit is {kwargs['fruit']}")
    
foo(veggie = 'Potato', fruit = 'Apple', animal = 'dog')

# we can use *variable and **variable in fuction simultaneosly

def  foo1(*args, **kwargs):
    print(f"I need {args[3]} {kwargs['grocery']}")
    
    
foo1(20,40,10,5,fruit = "apple", veggie = 'potato',grocery= 'eggs', animal = 'dog')

# remember to give arguments in same order as (*) and (**) are passed in the function

