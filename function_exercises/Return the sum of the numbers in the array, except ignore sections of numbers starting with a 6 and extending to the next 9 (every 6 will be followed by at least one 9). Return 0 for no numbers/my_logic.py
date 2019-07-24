#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 21:22:31 2019

@author: sandeep
"""

def summer_69(arr):
    sum1 = 0
    index = 0
    for item in arr:
        k = index
        if item == 6:
            for j in arr[k+1:]:
                if j ==9:
                    
                    index += 1
                    arr[index] = 0
                  #  print("index due to j==9 : ",index)
                    break
                else:
                    index += 1
                    # print("index due to j==9, else : ",index)
        
        # print(f"index for main loop: {index}")
        sum1 += arr[index]
        index +=1
        
        if index == len(arr):
            break
      
        
    return sum1 
        
# Check
print(summer_69([1, 3, 5]))

# Check
print(summer_69([4, 5, 6, 7, 8, 9]))

# Check
print(summer_69([2, 1, 6, 9, 11]))