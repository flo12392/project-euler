#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 11:23:01 2017

@author: florian
"""
d = 2
n = 3

total = 0

for i in range(1000):
    pd = d
    d = n + d
    n = d + pd
    
    if(len(str(n))>len(str(d))):
        print('n:' + str(n) + ', d: ' + str(d))
        total+=1