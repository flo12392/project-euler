string=''
k=1

while len(string)<1000000:
    string+=str(k)
    k+=1
    
indices = [string[10 ** k-1] for k in range(0,7)]    
product=1
for x in indices:
    product *= int(x)
