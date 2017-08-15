found=False

rangemax=6
n = 10
while not found:
   y = [set(list(str(n*x))) for x in range(1,rangemax+1)]
   union = set.union(*y)
   if(len(union)==len(y[0]) and all([x== [len(x) for x in y][0] for x in [len(x) for x in y]])): 
       found= True
   else:
       n+=1

print(n)
print(union)
print(y)   