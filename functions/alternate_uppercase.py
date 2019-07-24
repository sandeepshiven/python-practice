#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 17:21:08 2019

@author: sandeep
"""

def capital(string):
    new_string = []
    for letter in range(1,(len(string)+1)):
        if letter%2 ==0:
            new_string.append(string[letter-1].upper())
            
            
        else:
            new_string.append(string[letter-1].lower())
        
            
    return ''.join(new_string)  # 'whatever'.join(list)  returns a string after joining the list with whatever
        
    
st = input("Enter a string\n")
print("Changed string is \n{}".format(capital(st)))

