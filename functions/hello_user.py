#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 22:09:38 2019

@author: sandeep
"""

def hello(name = 'User'):
    print("Hello",name)
    
user=input("Enter user name\n")
hello(user)
hello()