#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 12:50:49 2017

@author: florian
"""
import math

N = 500
fraction = 3/7
result=[1,10]       
           
for n in range(3,N):
    n_min = math.floor(n*result[0]/result[1])
    n_max = math.ceil(n*fraction)
    for m in range(n_min,n_max+1):
        if(math.gcd(m,n)==1):
            if(m/n>result[0]/result[1] and m/n<fraction):
                print('n: ' + str(n) + ', m: ' + str(m))
                result[0] = m
                result[1] = n
                
print(result)