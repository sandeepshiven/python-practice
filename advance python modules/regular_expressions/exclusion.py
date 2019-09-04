#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:01:02 2019

@author: sandeep
"""

import re

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'

print(re.findall('[^!? ]+',test_phrase))
















