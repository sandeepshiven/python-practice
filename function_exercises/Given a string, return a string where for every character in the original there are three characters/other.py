#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 21:17:10 2019

@author: sandeep
"""

def paper_doll(text):
    result = ''
    for char in text:
        result += char*3   # modifying string as a whole
    return result


# Check
print(paper_doll('Hello'))

# Check
print(paper_doll('Mississippi'))