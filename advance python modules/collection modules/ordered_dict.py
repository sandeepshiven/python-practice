# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 16:59:18 2019

@author: sande
"""


from collections import OrderedDict

print("Normal dictionary")

d = {}

d['a'] = 1

d['b'] = 2

d['c'] = 3

d['d'] = 4

d['e'] = 5

d['f'] = 6
d['g'] = 7
d['h'] = 8
d['i'] = 9
d['j'] = 10
d['k'] = 11
d['l'] = 12
d['m'] = 13
d['n'] = 14
d['o'] = 15
d['p'] = 16
d['q'] = 17
d['r'] = 18
d['s'] = 19
d['t'] = 20
d['u'] = 21
d['v'] = 22
d['w'] = 23
d['x'] = 24
d['y'] = 25
d['z'] = 26
for key,value in d.items(): # not sure if return the values in the same order as entered
    print(key ,'=' ,value)



od = OrderedDict() # retains the order in which the elements are entered

od['d'] = 4

od['e'] = 5

od['f'] = 6
od['g'] = 7
od['h'] = 8
od['i'] = 9
od['j'] = 10
od['k'] = 11
od['l'] = 12
od['m'] = 13
od['n'] = 14
od['o'] = 15
od['p'] = 16
od['q'] = 17
od['r'] = 18
od['s'] = 19
od['t'] = 20
od['u'] = 21
od['v'] = 22
od['w'] = 23
od['x'] = 24
od['y'] = 25
od['z'] = 26

print('\n\n')
for key,value in od.items(): # sure return the values in the same order as entered
    print(key ,'=' ,value)

# equality with ordered dictionaries

'''

a regular dict looks at its contents when testing for equality.
an ordereddict also considers the order the items are added.
'''

print("Dictionaries are equal?")  
    
d1 = {} 

d1['a'] = 1
d1['b'] = 2

d2 = {}

d2['b'] = 2
d2['a'] = 1


print(d1==d2)

print("\nCheck again with ordered dict")

d1 = OrderedDict()

d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()

d2['b'] = 2
d2['a'] = 1


print(d1==d2) 