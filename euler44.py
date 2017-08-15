
import itertools
import pandas as pd

P = [int(x * (3*x-1)/2) for x in range(1,4000)]
Pset = set(P)

cont = True
n=7
result=[]

def difference(x):
    return(abs(x[0]-x[1]))

while n<9999:
    Px = P[:n]
    
    df = pd.DataFrame({'number1': P[:n], 'number2': [P[n] for x in range(n)] })
    df['diff'] = abs(df['number1']-df['number2'])
    df['sum'] = abs(df['number1']+df['number2'])
    
    df['sumx'] = df['sum'].apply(lambda x: x in Pset)    
    df['diffx'] = df['diff'].apply(lambda x: x in Pset)
    df = df[df.sumx & df.diffx]
    #print(n)
    if(len(df)>0):
        result.append(min(df['diff']))
        print(result)
        
    n+=1
        