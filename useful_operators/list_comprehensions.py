#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 15:49:17 2019

@author: sandeep
"""

string = "Sandeep"

my_list = []

for item in string:
    my_list.append(item)
    
print(my_list)
# above process can be done in a single line by using list comprehensions
my_list = []

my_list = [item for item in string]
print(my_list)

# example 1

lst = [x for x in "ikshit"]
print(lst)

lst = [x**2 for x in range(6)]
print(lst)

# example 2 can add if in list comprehension

lst = [x for x in range(11) if x%2 == 0]
print(lst)

# now order changes while using if else
lst = [x if x%2 == 0 else "odd" for x in range(11)]
print(lst)

# last example about nesting of loops
lst = []
for x in (1,2,3,4):     # more readable code always use this for readability 
    for y in  (1,10,100,1000):
        lst.append(x*y)
        
print(lst)


mylist = [x*y for x in (1,2,3,4) for y in (1,10,100,1000)]

print(mylist)









