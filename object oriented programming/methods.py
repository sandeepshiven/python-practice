#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 18:15:49 2019

@author: sandeep

"""


class Circle():
    pi = 3.14
    
    # circle gets initiated with radius one
    
    def __init__(self,radius = 1):
        self.radius = radius
        self.area = self.radius * self.radius * Circle.pi  # we can use self.circle but convention is class_name.(class object attribute)
       
     # method for resetting radius   
        
    def set_radius(self,new_radius):
        self.radius = new_radius
        self.area = self.radius * self.radius * Circle.pi
        
      # method for getting circumference  
    def get_circumference(self):
        
        return 2 * Circle.pi * self.radius
    
    
c = Circle()

print(f"Radius is {c.radius}")
print(f"Circumference is {c.get_circumference()}")
print(f"Area is {c.area}")

c2 = Circle()
c2.set_radius(2)

print(f"Radius is {c2.radius}")
print(f"Circumference is {c2.get_circumference()}")
print(f"Area is {c2.area}")







