# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 00:59:40 2019

@author: sande
"""

people_day = 1200000
people_total = 0

day = 1

def count_people(day,people_day,people_total):
    if day >365:
        return people_total
    return count_people(day +1,people_day,people_total+people_day)


total = count_people(day,people_day,people_total)

print(total)


















