#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 13:45:05 2017

@author: florian
"""

from sympy import sieve
import math

N=  5*10**7
n=math.ceil(N**0.5)*2
primes = list(sieve.primerange(1, n))

all_nums = set()

x=0
y=0
z=0

for x in range(len(primes)):
    y=0
    z=0
    while primes[x]**2 + primes[y]**3 + primes[z]**4 < N and y<len(primes):
        while primes[x]**2 + primes[y]**3 + primes[z]**4 < N and z<len(primes):
            all_nums.add(primes[x]**2 + primes[y]**3 + primes[z]**4)
            z+=1
        y+=1
        z=0