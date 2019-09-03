#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:32:23 2019

@author: sandeep
"""

import re

split_term = '@'

phrase = "sandeepshiven@gmail.com is my email"

print(re.split(split_term,phrase)) # splits the string from the position having split_term

# findall

find = 'match'

phrase2 ="This is first match, this is second match thats all"

print(re.findall(find,phrase2)) # returns list with find as many time it is found in phrase2

























