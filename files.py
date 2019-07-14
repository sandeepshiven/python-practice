#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 23:46:27 2019

@author: sandeep
"""

file = open('/media/sandeep/sandeep files/Complete-Python-3-Bootcamp-master/00-Python Object and Data Structure Basics/test.txt')
print(f"{file.read()}") # the file opens in default mode that is open
print(f"{file.read()}") # cursor has gone to the ende of the file we need to reset it at begining 
file.seek(0)

print(f"{file.read()}")
file.seek(0)

print(f"{file.readlines()}") # this method returns a list of the lines in the file
file.close()

file = open('/media/sandeep/sandeep files/Complete-Python-3-Bootcamp-master/00-Python Object and Data Structure Basics/test.txt','w+')
# w+ opens file in write and read mode so contents in a exsisting file is deleted or new file is created
print(f"{file.read()}")

file.write('This is a new line\n')

#file.seek(0)

file.write("Another line\n")
file.close()

file = open('/media/sandeep/sandeep files/Complete-Python-3-Bootcamp-master/00-Python Object and Data Structure Basics/test.txt','a+')
file.seek(0)

print(f"{file.read()}")

file.write("one more line")
file.close()

with open('/media/sandeep/sandeep files/Complete-Python-3-Bootcamp-master/00-Python Object and Data Structure Basics/test.txt','a+') as file:
    file.seek(0) 
    print(f"{file.read()}")
    file.seek(0)
    contents = file.read()
    print(f"{contents}")











