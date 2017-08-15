#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 11:23:01 2017

@author: florian
"""

def F(n,k):
    

x=[1]
k=0

for i in range(3,101):
   x.append(x[k] + math.floor(i/2)) 
   k+=1

df = pd.DataFrame({'x': range(2,101), 'y': x})
        