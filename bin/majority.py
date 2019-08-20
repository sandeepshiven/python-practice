# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 10:53:35 2019

@author: hp
"""

test_cases = int(input())

def find_majority():
    size = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    #print(arr)
    unique = set(arr)
    #print(unique)
    
    for i in unique:
        #print(i)
        num = arr.count(i)
        #print(f"num = {num}")
        if num > int(size/2):
            return int(i)
    return -1
        
        
for j in range(test_cases):
    result = find_majority()
    print(result)







