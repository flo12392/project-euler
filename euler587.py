#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 08:47:59 2017

@author: florian
"""

area =math.pi*0.5**2
area = (1-area)/4

import math
import scipy.integrate as integrate

n=1
perc=1
while(perc>0.001):
    n +=1
    x0=0
    y0=0
    x1=n
    y1=1
    h = 0.5
    k = 0.5
    r = 0.5
    
    a = (x1-x0)**2 + (y1-y0)**2
    b = 2*(x1-x0)*(x0-0.5) + 2*(y1-y0)*(y0-0.5)
    c = (x0-0.5)**2 + (y0-0.5)**2-r**2
    
    b24ac = (b**2-4*a*c)**0.5
    t1 = (-b-b24ac)/(2*a)
    t2 = (-b+b24ac)/(2*a)
    
    my_x = (x1-x0)*t1 + x0
    my_y = (y1-y0)*t1 + y0
    
    a1 = my_x*my_y*0.5
    a2 = integrate.quad(lambda x: 0.5-(0.5**2-x**2)**0.5, -0.5+my_x, 0)
    perc = (a1+a2[0])/area
    print(perc)
    
print(perc)
print(n)