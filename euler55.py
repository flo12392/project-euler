

def addPal(x):
    return(x+int(str(x)[::-1]))

def isPalindrome(x):
    return (str(x) == str(x)[::-1])

total=[]

for i in range(10,10000):
    found=False
    iters = 0
    x=i
    while not found  and iters<50:
        x = addPal(x)
        if(isPalindrome(x)):
            found=True
        else:
            iters+=1
        
    if not found:
        total.append(i)
        
print(total)
print(len(total))