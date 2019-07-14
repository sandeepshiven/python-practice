#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 23:13:10 2019

@author: sandeep
"""


x = 0

while x < 10:
    if x == 5:
        print("Currently x is 5")
        break  # break: Breaks out of the current closest enclosing loop
        
    else:
        print(f"{x} is less than 10")
        #continue   #continue: Goes to the top of the closest enclosing loop
        print("continuing...")
    x += 1
    
y = [2,4,5,6,7,8]
for num in y:
    pass # does nothing
    
print(num)    

    