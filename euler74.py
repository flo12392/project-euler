#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 16:43:04 2017

@author: florian
"""

def addfact(x):
    return(sum([math.factorial(int(y)) for y in list(str(x))]))

total=0
for i in range(1,1000000+1):    
    x = 1
    num = i
    this_set={num}
    while(len(this_set)==x):
        num = addfact(num)
        print(num)
        this_set.add(num)
        x+=1
 
    if(len(this_set)==60):
        total+=1
        print(i)
        
print(total)