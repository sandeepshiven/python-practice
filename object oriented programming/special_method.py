#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 13:20:51 2019

@author: sandeep
"""

class Book():
    
    def __init__(self,name,author,price):
        self.name = name
        self.author = author
        self.price = price
        
    def __len__(self):   # we can use the simple len(object) directly on class we first have to define 
        return self.price # so python can find its representation
    
    def __str__(self): # string representation of the Book class
        return f"The book's name is {self.name} and its author is {self.author}"
    
    def __del__ (self):  # del b would also work but this is done to give some additional information along with deletion
        print("A book is destroyed")
        
        
        
b = Book("Python Practice","Sandeep",68)

print(b)

#print(str(b))

print(len(b))

del b        












