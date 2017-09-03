#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 12:49:04 2017

@author: florian
"""

import math

n=10

while True:
    minimum = (0.5*(n-1)**2)**0.5
    maximum = (0.5*(n)**2)**0.5
    for x in range(math.floor(minimum), math.ceil(maximum)+1):
        if int(2*x*(x-1)) == int(n*(n-1)) :
            print(str(x) + ' / ' + str(n))
    n+=1
    
#15 / 21
#85 / 120
#493 / 697
#2871 / 4060
#16731 / 23661
#97513 / 137904
#568345 / 803761

# https://oeis.org/A011900

x = np.array([	1, 3, 15, 85, 493, 2871, 16731, 97513, 568345, 3312555, 19306983, 112529341, 655869061, 3822685023, 22280241075, 129858761425, 756872327473, 4411375203411, 25711378892991, 149856898154533, 873430010034205, 5090723162050695, 29670908962269963])
n = x[x>10**12][0]
(1/2)*(n+math.floor(math.sqrt(2)*n*math.floor(math.sqrt(2)*n)))
