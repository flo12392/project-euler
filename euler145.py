#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 17:34:05 2017

@author: florian
"""

maxn = 10**9

def check(x):
    if x % 10 ==0:
        return False
    else:
        return all([int(y) %2 ==1 for y in list(str(x+int(str(x)[::-1])))])
    
total = 0
for n in range(maxn):
    if(n % 1000000==0): print(int(n))
    if check(n):
        total+=1
        
print(total)