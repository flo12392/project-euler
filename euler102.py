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

