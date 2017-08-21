#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 15:30:21 2017

@author: florian
"""

import matplotlib.pyplot as plt

n1 = 2
n2 = 3
n3 = 4

def dec_to_bin(x):
    return bin(x)[2:]

def nimsum(n):
    n = [bin(x)[2:] for x in n]
    maxlength = max(len(x) for x in n)
    n = [x.rjust(maxlength, '0') for x in n]    
    results = [(int(n[0][x]) + int(n[1][x]) + int(n[2][x])) % 2 != 0 for x in range(maxlength)]   
    if(sum(results) == 0):
        return 0
    else:
        return 1

for power in range(12):
    total=0
    for n in range(1,2**power + 1):
        
        if n ^ 2*n ^ 3*n  ==0: # initially did minsum([n, 2*n, 3*n])
            total+=1

    print('power: ' + str(power) + ', total: ' + str(total))

x1 = 1
x2 = 1

for x in range(1,31):
    xnew = x2+x1
    x1=x2
    x2 = xnew
    print('power: ' + str(x) + ', total: ' + str(xnew))