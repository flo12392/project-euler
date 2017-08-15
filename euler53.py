import math

def func(n,r):
    return(int(math.factorial(n)/(math.factorial(r)*math.factorial(n-r))))

threshold = 1000000
max_n=100

total = 0

for n in range(1,max_n+1):
    over_threshold=False
    r=1
    while not over_threshold and r<=n:
        new_val = func(n,r)
        if new_val>threshold:
            over_threshold=True
            total += n+1 - 2*r
        else:
            r+=1
            
print(total)
