#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 14:43:07 2019

@author: sandeep
"""


try:
    file = open('testfile','w')
    file.write("Write a test file")
except TypeError: # will only run if there is an typeerror
    print("There was a type error!")
except OSError:
    print("Hey you have an OS Error!")
finally: # will execute no matter what
    print("I always run")


try:
    file = open('testfile','r')
    file.write("Write a test file")
except TypeError: # will only run if there is an typeerror
    print("There was a type error!")
except OSError:
    print("Hey you have an OS Error!")
finally: # will execute no matter what
    print("I always run")











