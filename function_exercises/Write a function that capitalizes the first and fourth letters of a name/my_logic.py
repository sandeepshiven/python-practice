#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 19:43:09 2019

@author: sandeep
"""

def old_macdonald(name):
    new_name = [i for i in name]
    new_name[0] = name[0].upper()
    new_name[3] = name[3].upper()
    return ''.join(new_name)


print(old_macdonald('macdonald'))
