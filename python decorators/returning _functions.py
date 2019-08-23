#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 18:06:28 2019

@author: sandeep
"""

def hello(name = "Sandeep"):
    
    
    def greet():
        return("\t This is inside 'greet()' function")
        
    def welcome():
        return("\t This is inside 'welcome()' function")
        
        
    if name == "Sandeep":
        return greet    # returning functions as a object
    
    else:
        return welcome
    
    
my_func = hello() # object assignment

print(my_func()) # will run greet object

my_func = hello("Ansh")

print(my_func()) # will run welcome object
        
        
        
        
        
        
        
        