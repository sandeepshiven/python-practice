#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 15:08:03 2019

@author: sandeep
"""

class Cylinder:
    
    pi = 3.14
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return (Cylinder.pi * ((self.radius )**2) * self.height)
    
    def surface_area(self):
        return ((2* Cylinder.pi *( self.radius **2))   +(2 * Cylinder.pi * self.radius * self.height) )

# EXAMPLE OUTPUT
c = Cylinder(2,3)

print("The volume of the cylinder is ",c.volume())

print("The total surface area of the cylinder is ",c.surface_area())