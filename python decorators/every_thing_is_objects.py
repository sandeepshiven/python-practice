#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 12:38:24 2019

@author: sandeep
"""

"""
in python everthing is a object
it means that functions are also objects 
and can be assigned lables and passed into other functions

"""



def hello(name = "Sandeep"):
    return "Hello " + name

get_function = hello # we are hello() function object to the 'get_function' variable


print(get_function())

del hello # deleting the hello function

print(get_function()) # still get_function is pointing to the original hello function 

print(hello()) # this will not run as the hello function is deleted



















 