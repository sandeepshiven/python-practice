#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 19:04:08 2019

@author: sandeep
"""


from collections import Counter


# counter with list 
my_list = [1,1,0,0,0,0,1,5,5,5,3,3,2,-2,2,-3,-3,-3,-2,3,8,9,9,-2,4,1,2,8,8,64,66,1,48,88,888,11,1,1,3,6,6,6,4,4,7]

print(Counter(my_list)) # prints the elements as keys and the number of time it repeats as value

# counter with strings

string = 'asdkfpwrksldnvaghhurtadsfnvaadfjkghiutahsdfkjvnkbvkjsdfhausiuastjkbvkjhdskjahkjvngjfsghughkcvn'

print('\n\n',Counter(string))


string1 = 'my name is sandeep shiven my name is sandeep sandeep is is is is my my'
 
print('\n\n',Counter(string1.split()))

c = Counter(string1.split()) # creates a counter object

print('\n\n',c)

print('\n\n',c.most_common(2),'\n\n') # returns list of the two most common 


list1 = Counter(my_list)

print(sum(list1.values()))  # total of all counts

print(list(list1)) # list of unique elements

print('\n\n',set(list1)) # convert to a set

print('\n\n',dict(list1))  # convert to regular dictionary

list2 = list1.items()

print('\n\n',list1.items()) # convert to a list of (elem,cnt) pairs

print('\n\n',Counter(dict(list2))) # coverts from a list of (elem,cnt ) pairs

print('\n\n',list1.most_common()[:-3-1:-1]) # n least common elements

list1 += Counter()

print('\n\n',list1)



