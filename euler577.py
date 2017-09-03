#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 12:56:20 2017

@author: florian
"""

#import math
#
#n = 20
#
#counter  = [] # for the simple pentagons
#counter2 = [] # for the not-so-simple pentagons
#total=0
#result=[]
#
#for i in range(3,n+1):
#    
#    if i % 3 == 0: 
#        counter.append(0)
#        if(i>3):
#            for j in range(int(i/3-1)):
#                counter2.append(0)
#    
#    counter = [x+1 for x in counter]
#    counter2 = [x+1 for x in counter2]
#    total+= sum(counter) + sum(counter2)
#    result.append(total)
#        
#print(total)


import math

n = 12345

counter = 0
total=0
result = 0
result2 = 0

for i in range(3,n+1):
    
    if i % 3 == 0: 
        counter+=1
        if(i>3):
            for j in range(int(i/3-1)):
                counter+=1
                
    total+=counter
    result+=total
    result2+=result
        
print(total)
print(result)
print(result2)