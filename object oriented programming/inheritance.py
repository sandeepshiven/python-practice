#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 22:47:50 2019

@author: sandeep
"""


class Animal(): # creating the base class
    
    def __init__ (self):
        print("Animal created")
        
    def who_am_i(self):
        print("Animal")
        
    def eat(self):
       print("Eating")
       
       
class Dog(Animal):  # dog class inheriting the properties of the animal class
    
    
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
        
    def eat(self):     # we can change the methods the of the base class by calling its exact name
        print("Dog is eating")
        
    def bark(self):    # we add new methods to the class
        print("Woof!")
        
        
        
anim = Animal()

anim.who_am_i()

anim.eat()

pussu = Dog()

pussu.who_am_i() # who_am_i() method inherited from the Animal class

pussu.eat()


pussu.bark()
















