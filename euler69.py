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

q = gen_primes()
val=1
while val<1000000:
    prev_val = val
    val = val * next(q)
    


#import pandas as pd
#
#
#def prime_factors(n):
#    i = 2
#    factors = []
#    while i * i <= n:
#        if n % i:
#            i += 1
#        else:
#            n //= i
#            factors.append(i)
#    if n > 1:
#        factors.append(n)
#    return factors
#
#def isPrime(n):
#    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
#
#primeslist  = []
#factorslist = []
#values = []
#maximum=1000000
#
#for n in range(2,maximum):
#    
#    if(n % 10000 ==0): print(n)
#    
#    if isPrime(n):
#        primeslist.append(n)
#        x = set()
#        x.add(n)
#        factorslist.append(x)
#        values.append(n-1)
#    else:
#        primes = set(prime_factors(n))
#       
#        this_factors = [factorslist[primeslist.index(x)] for x in primes]
#        values.append(n-len(set.union(*this_factors))-1)
#        
#        for prime in primes:
#            factorslist[primeslist.index(prime)].add(n)        
#        
#       
#
#            
#df = pd.DataFrame({'n':range(2,maximum),'phi':values})
#df['phin']=df['n']/df['phi']
#print(int(df.loc[np.argmax(df.phin)]['n']))
#    

# https://en.wikipedia.org/wiki/Euler's_totient_function