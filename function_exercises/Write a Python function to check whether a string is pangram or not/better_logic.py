#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 20:03:46 2019

@author: sandeep
"""
import string


def ispangram(str1, alphabet = string.ascii_lowercase ):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())

print(ispangram("The quick brown fox jumps over the lazy dog"))