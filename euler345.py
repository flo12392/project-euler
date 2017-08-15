import os
import numpy as np
import re
from scipy.optimize import linprog
from pulp import *

#abspath = os.path.abspath(__file__)
#dname = os.path.dirname(abspath)
#os.chdir(dname)

a = list(open("euler345.txt"))
mat = [x.rstrip('\n') for x in a]
mat = [re.sub(' +',',', x) for x in mat]
mat = [x.split(',') for x in mat]
mat = [[int(x) for x in rule] for rule in mat]

# 3315
mat = [[  7,  53, 183, 439, 863],
[497, 383, 563,  79, 973],
[287,  63, 343, 169, 583],
[627, 343, 773, 959, 943],
[767, 473, 103, 699, 303]]

x = [[str(i) + str(j) for i in range(len(mat))] for j in range(len(mat))]

prob = LpProblem("My problem", LpMinimize)

ingredient_vars = LpVariable.dicts("x",x,0,1,'Integer')
