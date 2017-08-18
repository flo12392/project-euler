#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 16:43:04 2017

@author: florian
"""

total=0
for i in range(1,10+1):
    for j in range(40):
        x=i**j
        if(len(str(x)))==j:
            total+=1
            print(x)
