#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 19:46:11 2019

@author: sandeep
"""

def old_macdonald(text):
    return text[:3].capitalize() + text[3:].capitalize()  # capitalize() capitalises the first letter in the string
#            Mac                        Donald

print(old_macdonald('macdonald'))