#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 11:17:36 2017

@author: florian
"""

import math
from sympy import sieve 
import pandas as pd


# how many times is x a prime factor of n
def findnumberfactors(n,x):
    total = 0
    while(n % x == 0):
            total+=1
            n = n/x          
    return(total)

def primefacs(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

total=0
N=100
primes = list(sieve.primerange(1, N+1)) 
s = [None]*N

for x in primes:
    s[x]=x

for x in primes:
    total = 0
    n=x
    pd.DataFrame({'x':range(n,math.floor(N-n)+1,x)})
    
    
    for n in range(x,N,x):
        


#n: 2, x: 2
#n: 3, x: 3
#n: 4, x: 4
#n: 5, x: 5
#n: 6, x: 3
#n: 7, x: 7
#n: 8, x: 4
#n: 9, x: 6
#n: 10, x: 5
#n: 11, x: 11
#n: 12, x: 4
#n: 13, x: 13
#n: 14, x: 7
#n: 15, x: 5
#n: 16, x: 6
#n: 17, x: 17
#n: 18, x: 6
#n: 19, x: 19
#n: 20, x: 5
#n: 21, x: 7
#n: 22, x: 11
#n: 23, x: 23
#n: 24, x: 4
#n: 25, x: 10
#n: 26, x: 13
#n: 27, x: 9
#n: 28, x: 7
#n: 29, x: 29
#n: 30, x: 5
#n: 31, x: 31
#n: 32, x: 8
#n: 33, x: 11
#n: 34, x: 17
#n: 35, x: 7
#n: 36, x: 6
#n: 37, x: 37
#n: 38, x: 19
#n: 39, x: 13
#n: 40, x: 5
#n: 41, x: 41
#n: 42, x: 7
#n: 43, x: 43
#n: 44, x: 11
#n: 45, x: 6
#n: 46, x: 23
#n: 47, x: 47
#n: 48, x: 6
#n: 49, x: 14
#n: 50, x: 10
#n: 51, x: 17
#n: 52, x: 13
#n: 53, x: 53
#n: 54, x: 9
#n: 55, x: 11
#n: 56, x: 7
#n: 57, x: 19
#n: 58, x: 29
#n: 59, x: 59
#n: 60, x: 5
#n: 61, x: 61
#n: 62, x: 31
#n: 63, x: 7
#n: 64, x: 8
#n: 65, x: 13
#n: 66, x: 11
#n: 67, x: 67
#n: 68, x: 17
#n: 69, x: 23
#n: 70, x: 7
#n: 71, x: 71
#n: 72, x: 6
#n: 73, x: 73
#n: 74, x: 37
#n: 75, x: 10
#n: 76, x: 19
#n: 77, x: 11
#n: 78, x: 13
#n: 79, x: 79
#n: 80, x: 6
#n: 81, x: 9
#n: 82, x: 41
#n: 83, x: 83
#n: 84, x: 7
#n: 85, x: 17
#n: 86, x: 43
#n: 87, x: 29
#n: 88, x: 11
#n: 89, x: 89
#n: 90, x: 6
#n: 91, x: 13
#n: 92, x: 23
#n: 93, x: 31
#n: 94, x: 47
#n: 95, x: 19
#n: 96, x: 8
#n: 97, x: 97
#n: 98, x: 14
#n: 99, x: 11