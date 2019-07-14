#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 21:00:29 2019

@author: sandeep
"""
sum1 = 0
tup = (1,2,4,5)
for t in tup:
    print(t)
    sum1 += t
    
print(sum1,"\n\n")

# example of tuple unpacking

list1 = [(2,4,),(6,8),(10,12)]

for t1 in list1:
    print(t1)

# now unpacking

print("\n\n")

for (t2,t3) in list1:
    print(t2)