import os
import numpy as np

#abspath = os.path.abspath(__file__)
#dname = os.path.dirname(abspath)
#os.chdir(dname)

a = list(open("euler99.txt"))
mat = [x.rstrip('\n') for x in a]
mat = [x.split(',') for x in mat]
mat = [[int(x) for x in rule] for rule in mat]

largest = mat[0]
largest_index=1

for i,new in enumerate(mat):
    # i have to do new = largest ** x
    x = math.log(new[0],largest[0])

    new_pow = new[1]*x
    
#    largest[0]**new_pow
#    new[0]**new[1]
    if new_pow>largest[1]:
        largest=new
        largest_index=i+1


print(largest)