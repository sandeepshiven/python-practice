# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 17:42:40 2019

@author: sande
"""

'''
standard tuple uses numerical indexes to access its members

but eack kind of namedtuple is represented by its own class
,it is a quick way of creating a new object/classes type with some attribute fields.

'''

from collections import namedtuple

Dog = namedtuple("Dog",'age breed name')
sam = Dog(name = "Sammy", age = 5, breed = 'bulldog')

print(f"My name is {sam.name}, my age is {sam.age}, my breed is {sam.breed}") 





















