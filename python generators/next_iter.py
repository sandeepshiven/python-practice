#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 22:27:28 2019

@author: sandeep
"""

def foo():
    for x in range(3):
        yield x

next_obj = foo()

print(next(next_obj))

print(next(next_obj))

print(next(next_obj))
#print(next(next_obj)) there will be stop iteration error at this point
# whihch indicates that all the values has been yielded 
try:
    print(next(next_obj))
except:
    print("Iteration has been stopped: StopIteration error\n\n")
    
string = "Sandeep"


for x in string:
    print(x)
    
# But that doesn't mean the string itself is an iterator! We can check this with the next() function
    
try:
    print(next(string))
except:
    print("\nTypeError: 'str' object is not an iterator\n\n")
    
'''
 this means that a string object supports iteration, 
 but we can not directly iterate over it as we could with a 
 generator function. The iter() function allows us to do just that!
'''
 
    
str_itr = iter(string) # making an iterable object

print(next(str_itr))

print(next(str_itr))

print(next(str_itr))    

print(next(str_itr))













