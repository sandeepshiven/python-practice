#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 18:21:03 2019

@author: sandeep
"""

# one .py

def func():
    print("FUNC() IN ONE.PY")
    
print("TOP LEVEL IN ONE.PY")

if __name__ == "__main__":
    print("ONE.PY IS BEING RUN DIRECTLY")
    
else :
    print("ONE.PY HAS BEEN IMPORTED")