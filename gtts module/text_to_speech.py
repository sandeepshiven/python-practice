#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 18:28:19 2019

@author: sandeep
"""

from gtts import gTTS

import os

fptr = open('test.txt','r')

my_text = fptr.read().replace('\n',' ')

language = 'en'

output = gTTS(text = my_text,lang = language,slow = False)

output.save("output.mp3")
fptr.close()

os.system("vlc output.mp3")











