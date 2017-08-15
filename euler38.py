numbers = range(9876)
result=[]

for x in numbers:
    k=1
    full=''  
    
    while(len(full)<9):
        full+=str(k*x)
        k=k+1
        
    if(len(full)==9  and k>2 and len(set(full) & set('123456789'))==9 ):
        result.append(full)
    
print(max(result))
