#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 18:29:06 2019

@author: sandeep
"""

def new_decorator(original_func):
    
    def wrap_func():
        
        print("Code here, would be executed before the func")
        
        
        original_func()
        
        
        print("Code here, would execute after the func\n\n\n")
        
    return wrap_func    
        
    
def func_needs_decorator():
    print("I want to be decorated")
    
decorator = new_decorator(func_needs_decorator)

decorator()


# simpler way to do line 24- 29 by using @ as on or off switch

@new_decorator
def func_needs_smart_decorator():
    print("Now I am smartly decorated")

func_needs_smart_decorator()










