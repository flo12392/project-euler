import os
import numpy as np
import re
from scipy.optimize import linprog
from pulp import *

#abspath = os.path.abspath(__file__)
#dname = os.path.dirname(abspath)
#os.chdir(dname)

a = list(open("data/euler345.txt"))
mat = [x.rstrip('\n') for x in a]
mat = [re.sub(' +',',', x) for x in mat]
mat = [x.split(',') for x in mat]
mat = [[int(x) for x in rule] for rule in mat]


x = [(i, j) for i in range(len(mat)) for j in range(len(mat))]

prob = LpProblem("My problem", LpMaximize)
x_vars = LpVariable.dicts("x",(range(len(mat)),range(len(mat))),0,1,'Integer')

# objective
for i in range(len(mat)):
    for j in range(len(mat)):
        prob.objective += x_vars[i][j]*mat[i][j]

for r in range(len(mat)):
        prob += lpSum([x_vars[r][v]for v in range(len(mat))]) <= 1,""
        
for c in range(len(mat)):
        prob += lpSum([x_vars[v][c]for v in range(len(mat))]) <= 1,""      
        
prob.solve()

print("Status:" + pulp.LpStatus[prob.status])
for v in prob.variables():
    print(v.name + "=" + str(v.varValue))
print("Total Cost =" + str(pulp.value(prob.objective)))
