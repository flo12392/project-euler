
def func(x):
    y = list(str(x))
    return(sum([int(n)**2 for n in y]))

total=0
set89 = set()

for i in range(2,10000000):
    x = i
    while x!=1 and x!=89:
        x = func(x)
        if(x in set89): x=89
        
    if x == 89:
        total+=1
        if i<600 :set89.add(i)