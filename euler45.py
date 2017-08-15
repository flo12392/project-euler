
import itertools
import numpy as np

T = np.array([int(x*(x+1)/2) for x in range(1,99999)])
P = set([int(x * (3*x-1)/2) for x in range(1,99999)])
H = set([int(x*(2*x-1)) for x in range(1,99999)] )       

T[np.where([x in P and x in H for x in T])]
