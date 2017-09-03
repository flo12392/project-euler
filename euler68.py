#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 18:23:26 2017

@author: florian
"""
import numpy as np
import copy

global all_solutions
all_solutions=[]

def finish_ring(solution,total,gon):
    solution2 = copy.copy(solution)
    options_left = {1,2,3,4,5,6,7,8,9,10} - set(np.unique(solution2))
    if(gon==len(solution2)-2):
        for x in options_left:
            if x + solution2[gon][2] + solution2[0][1] == total:
                solution2[gon+1] = [x,solution2[gon][2],solution2[0][1]]
                all_solutions.append(solution2)
    
    for x in options_left:
        for y in options_left:
            if x != y:
                if(x+y+solution2[gon][2]==total):
                    solution2[gon+1] = [x,solution2[gon][2],y]
                    finish_ring(solution2,total,gon=gon+1)
                    

for start in range(1,11):
    for x in range(1,11):
        for y in range(1,11):
            if x != y and y != start and x != start:
                init_sol = [[start,x,y],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
                total = sum(init_sol[0])
                finish_ring(init_sol,total,gon=0)

for z in range(len(all_solutions)):
    x = all_solutions[z]
    minimum = np.argmin([y[0] for y in x])
    if minimum !=0:
        all_solutions[z] = x[minimum:] + x[:minimum]

max_found = 0
for x in all_solutions:
    result = []
    for y in x:
        for z in y:
            result.append(str(z))
    if(int(''.join(result))>max_found) and len(''.join(result))==16 :
        max_found = int(''.join(result))
        
print(max_found)

