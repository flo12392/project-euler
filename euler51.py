from collections import Counter
import itertools
import numpy as np
import math

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """

    D = {}
    q = 2
    
    while True:
        if q not in D:

            yield q
            D[q * q] = [q]
        else:

            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        
        q += 1

def find_indices(string,chartofind):
    return([pos for pos, char in enumerate(string[:-1]) if char == chartofind])

def all_combinations(stuff):
    result = []
    for L in range(1, len(stuff)+1):
      for subset in itertools.combinations(stuff, L):
        result.append(subset)
    return(result)

from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

found = False
number_primes = 8
g = gen_primes()
for x in range(4): next(g)

while not found:
    x = next(g)
    no_digits = int(math.log10(x))+1
    strx = np.array(list(str(x)))
    unique = list(set(strx[:-1]))
    indices = [find_indices(strx,x) for x in unique]
    
    for i in range(len(unique)):
        all_combs = all_combinations(indices[i])
        #print('\n\n\ni =  ' + str(i) + ', all_combs = ' + str(all_combs))
        min_number = -1
        for j in range(len(all_combs)):
            #print('j =  ' + str(j) + ', all_combs[j] = ' + str(all_combs[j]))
            total=0
            for val in range(10):
                stry = np.array(strx)
                stry[list(all_combs[j])] = val           
                thisnumber = int(''.join(stry))  
                #print('checking' + str(thisnumber))
                if isPrime(thisnumber) and int(math.log10(thisnumber))+1==no_digits:
                    total+=1
                    #print('its a prime! total: ' + str(total))
                    if(min_number==-1 and found==False): min_number = thisnumber
                    if total>= number_primes: 
                        found=True
                        final = min_number
                        
print(final)