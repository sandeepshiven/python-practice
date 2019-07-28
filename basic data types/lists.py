#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 22:38:35 2019

@author: sandeep
"""

my_list=[1,'one',2,'two',3,'three',4,'four',5,'five']

print(f"The list :{my_list}")

print(f"Length of the list: {len(my_list)}")

print(f"Now element at index 5:{my_list[5]}")

print(f"Now some slicing examples:- \n{my_list[2::2]}\n{my_list[:4]}\n{my_list[2:4]}")

print(f"Now a example of concatenation:\n{my_list+['sandeep']}") # this does not changes the original list

print(f"{my_list}")

my_list = my_list + ['sandeep']

print(f"Now some reassingment:\n{my_list}")

print(f"Making the list double:\n{my_list*2}")  # This does not change the actual list 

print(f"Now some list methods:")

my_list.append('shiven') #appends the argument given in .append() to the last of the list

print(f"The appending:\n{my_list}")

my_list.pop(5) # pops out or delete the item at given index the default index is -1
                # now this poped out value can be assined to the variable like this: var=list.pop()//
print(f"The poping:\n{my_list}")

my_list.reverse()

print (f'Revesing the list:\n{my_list}')
new_list = [1,3,5,2,4,52,567,546,325,6747,3]

print(f"Sorting of list:\n{new_list}")

new_list.sort()
print(f'{new_list}')

mult_D = [[3,324,.23,235.32],['sandeep','shiven','unni'],['sandeep',23.324,'shiven',34,'unni',432]]

print(f'The multidimensional array:\n{mult_D}')

print(f"Grabbing a single list:\n{mult_D[1]}")
 
print(f"Now grabbing a single element:\n{mult_D[2][3]}")