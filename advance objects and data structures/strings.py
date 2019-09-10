#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 20:25:35 2019

@author: sandeep
"""

s = 'hello world'


print(s.capitalize()) # capitalize() doesn't capitalizes permanantly


print(s.upper()) # not permanant

print(s.lower()) # not permanant

# above examples shows that strings are immutable

s = s.upper() # this changes everthing
print(s)

s = s.lower()
print(s)

# location and counting

print(s.count('o')) # counts the occurence of the argument given

print(s.find('o')) # prints the index of the first occurence of the argument

# formatting

print(s.center(20)) # by default centers the string with whitespaces

print(s.center(20,'s')) # takes only one char string and centers the
                        # the provided strings in between the no. of argument

print('hello\thi')


#is check methods

s = 'Hello'

print(s.isalnum()) # check for alphanumeric string


print(s.isalpha()) # check for all characters are alphabets

print(s.islower()) # checks if all char is lowercase

print(s.isspace()) # checks if all char is whitespace

print(s.istitle()) 
'''

istitle() will return True if s is a title cased string and there is 
at least one character in s, i.e. uppercase characters may only 
follow uncased characters and lowercase characters only cased ones
. It returns False otherwise
'''

print(s.isupper()) # checks if all is upper case

print(s.endswith('o')) 


