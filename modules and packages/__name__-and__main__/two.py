#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 18:21:44 2019

@author: sandeep
"""
# TWO.PY

import one

print("TOP LEVEL IN TWO.PY")

one.func()

if __name__ == "__main__":
    print("Two.py is being run directly")
    
else:
    print("Two.py has been imported")
                           