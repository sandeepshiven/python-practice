#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 21:34:31 2019

@author: sandeep
"""


def get_cubes(n):
    result = []
    for i in range(1,n+1):
        result.append(i**3)
    return result
        
for x in get_cubes(10):
    print(x)

'''

the above method is not efficient for memory
first a list is created then appended after that whole list
is returned, and then each element is iterated for printing.

But by using generator we can stop the execution of the function
and return the current result of the execution and store the point
at which the execution is stopped and then we can resume our execution 


we are not storing the list as above instead we are operating on the value as it comes

'''

def get_cubes_again(m):
    
    for j in range(1,m+1):
        yield(j**3)
        
print("\n\n\n")

for y in get_cubes_again(10):
    print(y)
    
    
print("\n\n")
    
print(get_cubes_again(10))

print('\n',list(get_cubes_again(10)))  # yeah we can create a list by it
        
        












