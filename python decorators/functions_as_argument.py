#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 18:17:51 2019

@author: sandeep
"""


def hello():
    return "Hello Sandeep"


def func(re_func):  # passing some other function as argument
    
    print('Other code will go here')
    
    print(re_func())
    
    
func(hello)  # we have to pass raw function not run function as hello()













