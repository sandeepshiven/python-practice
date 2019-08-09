#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 02:29:06 2019

@author: sandeep
"""

  # polymorphism refers to the way in which different object classes can share the same method name, and those methods can be called from the same place even though a variety of different objects might be passed in
class Dog():
    
    def __init__(self,name):
        self.name = name
        
    def speak(self):   
        return self.name + " says woof!"
        
        
class Cat():
    
    
    def __init__(self,name):
        self.name  = name
        
    def speak(self):     # same method name as Dog class
        return self.name + " says meow!"
    
    
spike = Dog("Spike")
print(spike.speak())

tom = Cat("Tom")


print(tom.speak()) 
        
        
        
        













