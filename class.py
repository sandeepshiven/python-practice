#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 18:22:11 2019

@author: sandeep
"""
class Robot:
    def __init__(self,name,color,weight): # arrtibutes are in brackets and below are constructor
        self.name = name
        self.color = color
        self.weight = weight
    
    def introduce_self(self):   # method
        print("My name is " + self.name)
        


r1 = Robot("Tom","red",30)
r2 = Robot("Jerry","blue",40)

r1.introduce_self()
r2.introduce_self()

class Person:
    def __init__(self,name,personality,is_sitting,robot_owned):
        self.name = name
        self.personality = personality
        self.is_sitting = is_sitting
        Robot.robot_owned = robot_owned  # a Robot type varaiable
        
    def owned_robot(self):
        print(self.name + " owns " + self.robot_owned.name)  # the self.robot_owned.name gets the name of the robot from the robot type variable
    
p1 = Person("Alice", "aggressive", False,r2)
p2 = Person("Becky", "aggressive", True,r1)
   

p1.robot_owned = r2
p2.robot_owned = r1

p1.owned_robot()
p2.robot_owned.introduce_self()  # same as writting r1.introduce_self()
    