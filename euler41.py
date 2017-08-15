from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

import itertools
mylist=list(itertools.permutations([1,2,3,4,5,6,7,8,9])).reverse
#mylist = mylist[0:100]

result=[]
found = False
k=0

while not found:
    if(isPrime(int(''.join([str(x) for x in mylist[0]])))):
        result = int(''.join([str(x) for x in mylist[0]]))
        found=True
    else:
        k+=1
 