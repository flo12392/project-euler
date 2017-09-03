from pulp import *

a = list(open("euler96.txt"))
mat = [x.rstrip('\n') for x in a]

# read text file
sudokus = []
k=-1
for x in mat:
    if 'Grid' in x:
        k+=1
        sudokus.append([])
    else:
        sudokus[k].append([int(y)  for y in list(x)])
      
# create grid for boxes        
grid = ((0,1,2),(3,4,5),(6,7,8))
boxes =[]
for i in range(3):
    for j in range(3):
        x = grid[i]
        y = grid[j]
        boxes.append([(i,j) for i in x for j in y])
        

all_nums=[]

for sudoku in sudokus:
    
    prob = LpProblem("Sudoku", LpMaximize)
    x_vars = LpVariable.dicts("x",(range(9),range(9),range(1,10)),0,1,'Integer')
    
    # objective
    prob.objective = 0 
    
    # all rows contain values 1-9
    for z in range(1,10):
        for j in range(9):
            prob += lpSum([x_vars[i][j][z] for i in range(9)]) <= 1,""
            
     # all columns contain values 1-9        
    for z in range(1,10):
        for i in range(9):
            prob += lpSum([x_vars[i][j][z] for j in range(9)]) <= 1,""
    
    # only one number per index      
    for i in range(9):
        for j in range(9):
            prob += lpSum([x_vars[i][j][z] for z in range(1,10)]) == 1,""
            
    # box constrains         
    for z in range(1,10):
        for box in boxes:
            prob += lpSum([x_vars[i][j][z] for (i,j) in box]) == 1,""

    # fixed numbers:
    for i in range(9):
        for j in range(9):
            z = sudoku[i][j]
            if(z>0):
                prob += x_vars[i][j][z] ==1,""
                                 
    prob.solve()
    
    num=[]
    for j in range(3):
        for z in range(1,10):
            if(value(x_vars[0][j][z])>0):
                num.append(z)                       
    all_nums.append(int(''.join([str(x) for x in num])))
    
print(sum(all_nums))
            
    
