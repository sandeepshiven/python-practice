#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 14:27:13 2019

@author: sandeep
"""

def up_low(s):
    upper_count=0  # can use dictionary d={'upper': 0, 'lower':0}
    lower_count = 0
    string = [i for i in s] # no need to do this can use this
    for i in string:        # for i in s:
        if i.isupper():
            upper_count +=1
        elif i.islower():
            lower_count += 1
        else:
            continue
    print(f"Original String : {s}")
    print(f"No. of Upper case characters : {upper_count}")
    print(f'No. of Lower case characters : {lower_count}')
            

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)
