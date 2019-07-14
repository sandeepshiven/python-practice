#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 18:11:25 2019

@author: sandeep
"""
my_list = [1,2,3,4,5,6,7,8,9,10,'sandeep','ikshit']

for abc in my_list:   # naming of the variable is not important we can give it any name
    print(abc)   # in place of abc we can print a string or anything
    print('string')
    print(f"{my_list}")

print("\n\n\n\n")

my_list = [1,2,3,4,5,6,7,8,9,10]
print("A program for printing even and odd numbers in the list\n" )

for list1 in my_list:
    if list1 % 2 ==0:
        print(f"Even number: {list1}")
    else:
        print(f"Odd number: {list1}")
        
        
print("\n\n\n\n\nA program for calculating sum of the list")

list_sum = 0
for value in my_list:
    list_sum += value
    print(f"List sum ={list_sum}")
    
print(f"Final sum = {list_sum}")

print("Now printing the string letter by letter")

for string in "My name is Sandeep Shiven":
    print(string)
    
    
    
    

