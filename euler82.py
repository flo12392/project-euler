import os
import numpy as np

#abspath = os.path.abspath(__file__)
#dname = os.path.dirname(abspath)
#os.chdir(dname)

a = list(open("data/euler82.txt"))
mat = [x.rstrip('\n') for x in a]
mat = [x.split(',') for x in mat]
mat = [[int(x) for x in rule] for rule in mat]

#mat = [[1,3,9],[9,2,9],[9,1,3]]

for colx in range(1,len(mat)):
    newcolx = [99999999 for x in range(len(mat))]
    
    for tox in range(0,len(mat)):
        for fromx in range(0,len(mat)):
            start = mat[fromx][colx-1]
            addition=0
            if tox>fromx: addition = sum([row[colx] for row in mat[fromx:tox+1]])
            if fromx>tox: addition = sum([row[colx] for row in mat[tox:fromx+1]])
            if fromx==tox: addition = mat[tox][colx]
                    
            new_val = start+addition
            if new_val < newcolx[tox]: newcolx[tox] = new_val
   
    for i,x in enumerate(newcolx):
       mat[i][colx] = x
                
                    
                    
np.matrix(mat)
min([x[len(mat)-1] for x in mat ])
