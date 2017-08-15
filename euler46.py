def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

search = 4
n=1
found=False
factors = [set()]*search

while not found:
    factors.append(set(prime_factors(n)))
    del factors[0]
    
    if(all([len(x)==search for x in factors])):
        print('found: ' + str(n-search+1))
        found=True
    else:
        n+=1

    
    
