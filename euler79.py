import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

a = list(open("euler79.txt"))
rules = [x.rstrip('\n') for x in a]
rules = [list(x) for x in rules]
strip = 0
pw0=''.join([x[0] for x in rules])
pw1=''.join([x[1] for x in rules])
pw2=''.join([x[2] for x in rules])
password = pw0 + pw1 + pw2


while strip < len(password):
    password_new = password[:strip] + password[strip+1:]
    still_valid=True

    for rule in rules:
        check = True
        ind1 = np.where(np.array([x==rule[0] for x in password_new]))[0]
        ind2 = np.where(np.array([x==rule[1] for x in password_new]))[0]
        ind3 = np.where(np.array([x==rule[2] for x in password_new]))[0]
        
        if len(ind1)>0:            
            first_ind2 =  ind2[ind2>min(ind1)]
            if len(first_ind2)>0: 
                first_ind2 = first_ind2[0] 
                first_ind3 =  ind3[ind3>first_ind2]
                if not len(first_ind3)>0: check=False
            else: 
                check=False
            
            if not check:
                still_valid=False
        else:
            still_valid=False
            
    if still_valid:
        password = password_new
    else:
        strip+=1
        
print(password)
