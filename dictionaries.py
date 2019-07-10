#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 00:13:26 2019

@author: sandeep
"""

my_dict = {"key1":1234,'key2':3.43,'key3':'sandeep','key4':[1,3.4,'Ikshit'],'key5':{'key6':'anything'}}

print(f"{my_dict}")
print(f"Grabbing a dictonary element by a key:\n{my_dict['key2']}")

print(f"Printing a specific element from the list inside the dictionary:\n{my_dict['key4'][2]}")
# can do same for dictionaries inside a dictionary e.g. my_dict['key5']['key6']

print(f"Now grabbing a single element and convertiing it  into uppercase:\n{my_dict['key4'][2].upper()}")

#this change is not permanent

# Now playing with values of key
my_dict['key1'] -= 1000

my_dict['key3'] = 'shiven'

# finally adding a new key
my_dict['key7']='new'

print(f"{my_dict}")

print(f'{my_dict.keys()}' )  # shows keys in a dictionary

print(f'{my_dict.values()}') # shows values inside the dictionary

print(f'{my_dict.items()}') # shows keys and values in pair















