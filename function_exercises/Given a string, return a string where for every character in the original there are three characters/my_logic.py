#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 21:12:05 2019

@author: sandeep
"""

def paper_doll(text):
    string = [st for st in text]
    insert = []
    for i in range(len(string)): # first loop attaches one word
        insert.append(string[i])
        for j in range(2):  # this appends two more same words making a total of three
            insert.append(string[i])
    return ''.join(insert)
# Check
print(paper_doll('Hello'))

# Check
print(paper_doll('Mississippi'))