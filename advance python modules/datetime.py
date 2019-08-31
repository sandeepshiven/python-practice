#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:37:19 2019

@author: sandeep
"""

from datetime import datetime

#datetime object cotaining current date and time

now = datetime.now()

print("now =",now)

#dd/mm/yy H:M:S
c_time = now.strftime("%d/%m/%Y   %r")
print(c_time)










