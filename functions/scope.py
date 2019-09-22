#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 23:00:59 2019

@author: sandeep
"""

x = 35 # global declaration
def printer():
    x =9889    # local declaration (different from the global x)
    return x

print(x)
print(printer())


f = lambda x:x**2  # x is local here

# example of enclosing variable

name = 'This is a global variable' 

def greet():
     name = "Sandeep" # enclosing function local declaration

# now to use the global variable use 'global x' as declaration
     
     def hello():
         print("Hello "+name)
    
     hello()
    
print(name)
greet()

# python reserves some of the key words and does not overwrite it e.g. len,print,return etc.

x = 50
def func(x):
    print ('x is',x)
    x = 3  # this change is local
    print('Changed local x to',x)


func(x)

print('x is still',x)

# writi ng the above function again using the global function

x = 50
def func1(): # don't pass x in the function
    global x
    print ('x is',x)
    x = 3
    print('Changed local x to',x)


func1()


print('Now x is changed to',x)

func1()


print('Now x is changed to',x)
