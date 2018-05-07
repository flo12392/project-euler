import os
import numpy as np

#abspath = os.path.abspath(__file__)
#dname = os.path.dirname(abspath)
#os.chdir(dname)

a = list(open("data/euler81.txt"))
mat = [x.rstrip('\n') for x in a]
mat = [x.split(',') for x in mat]
mat = [[int(x) for x in rule] for rule in mat]
mat1 = np.matrix(mat)


start = [0,0]
step = 1
stop=False

while not stop:
    step+=1
    
    xcoords = np.array(range(step))
    ycoords = np.array(range(step))[::-1]
    to_keep = (xcoords<80) & (ycoords<80)
    xcoords = xcoords[to_keep]
    ycoords = ycoords[to_keep]

    for (x,y) in zip(xcoords,ycoords):
        
        if x<80 and y<80:
            left = (y,x-1)
            up = (y-1,x)
            
            if(up[0]<0):
                mat[y][x] = mat[y][x-1] + mat[y][x]
                
            if(left[1]<0):
                mat[y][x] = mat[y-1][x] + mat[y][x]
                
            if(left[1]>-1 and up[0]>-1):
                mat[y][x] = mat[y][x] + min(mat[y][x-1],mat[y-1][x])
  
        if x == 79 and y == 79:
            stop = True