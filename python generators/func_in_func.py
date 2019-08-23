#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 13:01:05 2019

@author: sandeep
"""


def hello():
    print("This 'hello()' function is being executed")
    
    def greet():
        return("\t This is inside 'greet()' function")
        
    def welcome():
        return("\t This is inside 'welcome()' function")
        
    print(greet())
    print(welcome())
    print("The function 'hello()' has been ended")


hello()


welcome() # this will not run as this function was locally defined inside the hello function







