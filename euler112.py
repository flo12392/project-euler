#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 09:49:15 2017

@author: florian
"""

def bouncy(x):
    x=list(str(x))
    if all(x[i] <= x[i+1] for i in range(len(x)-1)) or all(x[i] >= x[i+1] for i in range(len(x)-1)):
        return False
    else:
        return True
    
total = 0
i=1

while total/i!=0.99:
    i+=1
    if(bouncy(i)): total+=1

print(i)    