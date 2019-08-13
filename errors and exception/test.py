#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 22:25:07 2019

@author: sandeep
"""

import unittest

import test_case

class TestCap(unittest.TestCase):  # inheriting the properties of class TestCase in unit test module
    
    def test_one_word(self):
        text = 'python'
        result = test_case.func(text)
        self.assertEqual(result,'Python')   # this compares the arguments passed
        
    def test_multiple_word(self):
        text = 'monty python'
        result = test_case.func(text)
        self.assertEqual(result,'Monty Python')
        
        
        

if __name__ == '__main__':
    unittest.main() # this provides command line interface











