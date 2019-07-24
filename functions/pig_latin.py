#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 23:01:25 2019

@author: sandeep
"""

def pig_latin(word):
    first_word = word[0]
    
    if first_word.lower() in 'aeiou':
        pig_word = word + 'ay'
        
    else:
        pig_word = word[1:] + first_word + 'ay'
        
        
    return pig_word

print(pig_latin(input("Enter a word to convert into pig latin\n")))