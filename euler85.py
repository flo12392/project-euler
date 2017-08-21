def rects(x,y):   
    tot=0
    for i in range(1,x+1):
        for j in range(1,y+1):
            if i!=j:
                tot+=(x-i+1)*(y-j+1)
                
    for z in range(1,min(x,y)+1):
        tot +=(x-z+1)*(y-z+1)
    return(tot)


error=10000
top = (-1,-1)

for i in range(100):
    for j in range(100):
        if abs(rects(i,j)-2000000)<error:
            error = abs(rects(i,j)-2000000)
            top = (i,j)
            print(top)
            print(error)