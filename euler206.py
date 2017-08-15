minimum = math.floor(sqrt(1121314151617181910))
maximum = math.ceil(sqrt(1929394959697989990))
minimum = int(math.ceil(minimum / 10.0)) * 10
maximum = int(math.ceil(maximum / 10.0)) * 10

for i in range(minimum,maximum,10):

    mylist  = list(str(i**2)) 
    if(all([str((x+1) % 10) == str(y) for x,y in enumerate(mylist[::2])])): break

print(i)