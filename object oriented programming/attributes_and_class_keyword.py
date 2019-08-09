#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 15:07:04 2019

@author: sandeep
"""

class Student(): # object Student
    
    study = "engineering"  # common for every Student instance  (Class object attribute)
    
    def __init__(self,name,roll,branch):
        
        #attributes
        # we take in arguments and
        # assing it using self.attributes_name
        
        self.name = name
        self.roll = roll
        self.branch = branch
        
# Student instance
stu1 = Student("Sandeep", 98 ,"CSE")

print(f"My name is {stu1.name}. I am persuing {stu1.study}  my branch is {stu1.branch} and my roll no. is {stu1.roll}")
print(f"{type(stu1)}") 