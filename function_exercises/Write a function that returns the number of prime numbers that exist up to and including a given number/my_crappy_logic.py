#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 21:59:44 2019

@author: sandeep
"""

def count_primes(num):
    count = 0
    primes = []
    for number in range(2,num+1):
        for item in range(2,number):
            if number % item == 0:
                break
        else:        
            count += 1
            primes.append(number)
    print(primes)
    return count
                
        
                

# Check
print(count_primes(100))

'''
def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
    
'''


'''

def count_primes2(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:  # use the primes list!
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
    
'''