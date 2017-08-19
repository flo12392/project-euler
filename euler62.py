#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 17:41:55 2017

@author: florian
"""


digits=3
find = 4

found = False

while not found:
    print(digits)
    this_cubes = [x**3 for x in range(math.ceil((10**digits)**(1/3)), math.ceil((10**(digits+1))**(1/3)))]
        
    for x in range(len(this_cubes)):
        total=0
        for y in range(x+1,len(this_cubes)):
            if (sorted(str(this_cubes[x])) == sorted(str(this_cubes[y]))):
                total+=1
                if(total==find):
                    print('Found! smallest cube: ' + str(this_cubes[x]))
                    found=True
            
    digits+=1