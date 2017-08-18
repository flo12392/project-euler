from sympy import sieve
import numpy as np

primes = list(sieve.primerange(1, 10**8))
primes2 = np.array(primes)
primes2 = primes2-1
primes = set(primes)

total=0

for n in primes2:
    is_ok=True
    d=1
    d_max = int(math.sqrt(n) + 1)
    
    while d <= d_max and is_ok:
        if n % d == 0:
            if(int(d +n/d) not in primes):
                is_ok = False
        d+=1
    if(is_ok): total+=n
   # print('n: ' + str(n) + ', is_ok: ' + str(is_ok))

print(total)