#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 19:01:18 2019

@author: sandeep
"""

import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-80)
voices = engine.getProperty('voices')
count = 0
'''for voice in voices:
    print(count)
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
    count += 1
'''

engine.say("India is my country. All indians are my brothers and sisters")
engine.runAndWait()













