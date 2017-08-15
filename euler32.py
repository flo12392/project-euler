import pandas as pd
import numpy as np

import itertools
mylist=list(itertools.permutations([1,2,3,4,5,6,7,8,9]))
#mylist = mylist[0:100]

result=[]

for x in mylist:
    a = x[0]*10 + x[1]
    b = x[2]*100 + x[3] * 10 + x[4]
    c = x[5]*1000 + x[6]*100 + x[7] * 10 + x[8]
    
    if a*b==c: result.append(c)
    
    a1 = x[0]
    b1 = x[1] * 1000 + x[2]*100 + x[3] * 10 + x[4]
    c1 = x[5]*1000 + x[6]*100 + x[7] * 10 + x[8]
    
    if a1*b1==c1: result.append(c)
    

print(sum(set(result)))