#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 22:28:37 2019

@author: sandeep
"""


list1 = ["a",'b','c','d','e','f']
list2 = [1,2,34,5]

print(f"{list(zip(list1,list2))}") # zip returns list,tuples of tuples or dictionary after, ziping two lists

# the size of the returned list is same as the shortest list given in the argument

for first,second in zip(list1,list2):
    print(f"{first} and {second}")


