#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 20:09:42 2019

@author: sandeep
"""

print('hello')
string='abcdefghijklmnopqrstuvwxyz'
print('sliced string:')
print(string[4:])
print("length of srtring:")
print(len(string))
print("reversed string")
print(string[::-1])
name = "Sandeep Shiven"
print(name.split('e'))
print("Name is " + name)
print("%d %f %s %s"%(1,32.63,'sandeep',name))
print("%10.3f"%64.34534534)
print("{} {} {}".format('sandeep','shiven',name))
print("{1} {0}".format('sandeep','shiven'))
print("{b} {a} {c}".format(a='sandeep',b='shiven',c=name))
print("{!r} {!r}".format('sandeep','shiven'))
print('{0:8} | {1:10}'.format('Fruit', 'Quantity'))
print("{0:9.4f} {1:7.2f}".format(4.7,89.09843))
print(f"{name}")
print(f"{name!r}")
num = 63.092353098
print(f"result:{num:{10}.{6}}")