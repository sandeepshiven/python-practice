#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 15:05:12 2019

@author: sandeep
"""

class Line:
    
    def __init__(self,coor1,coor2):  # should've used tuple unpacking
        self.x1 = coor1[0]
        self.y1 = coor1[1]
        self.x2 = coor2[0]
        self.y2 = coor2[1]
    
    def distance(self):
        return (((self.x2 - self.x1)**2  +  (self.y2 -self.y1)**2)**(0.5))
    
    def slope(self):
        return ((self.y2 -self.y1)/(self.x2 - self.x1))

# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print("Distance between the coordinates is " , li.distance())

print("Slope of the line joining the coordinates is " , li.slope())