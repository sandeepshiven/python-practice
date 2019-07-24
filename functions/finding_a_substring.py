#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 22:26:08 2019

@author: sandeep
"""

def substring(string,sub):
    if sub.lower() in string.lower():
        return "Yes, the word is in the string"
    else:
        return "No, the word is not in the string"
    
    
st = input("Enter a string\n")
su = input("Enter the word or string you want find\n")
print(substring(st,su))


# better way

def better(st,su):
    return su.lower() in st.lower()


print(better(st,su))
        
        
        
        