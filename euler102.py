import os
import numpy as np
import re
from scipy.optimize import linprog
from pulp import *

#abspath = os.path.abspath(__file__)
#dname = os.path.dirname(abspath)
#os.chdir(dname)

import matplotlib.path as mplPath
import numpy as np

poly = [190, 50, 500, 310]
bbPath = mplPath.Path(np.array([[poly[0], poly[1]],
                     [poly[1], poly[2]],
                     [poly[2], poly[3]],
                     [poly[3], poly[0]]]))

bbPath.contains_point((200, 100))

a = list(open("euler102.txt"))
mat = [x.rstrip('\n') for x in a]
mat = [re.sub(' +',',', x) for x in mat]
mat = [x.split(',') for x in mat]
mat = [[int(x) for x in rule] for rule in mat]


total=0
for line in mat:
    a = line[0:2]
    b = line[2:4]
    c = line[4:6]
    path = mplPath.Path([a,b,c])
    if(path.contains_point((0,0))):
        total+=1

print(total)
