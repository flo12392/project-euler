
def add_diagonal(x,diagonal):
    x=x-1
    prev_max = max(diagonal)
    new_diag = list(range(prev_max+x,prev_max+5*x,x))
    return(diagonal + new_diag)

def isprime(n):
    '''check if integer n is a prime'''

    # make sure n is a positive integer
    n = abs(int(n))

    # 0 and 1 are not primes
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2: 
        return True    

    # all other even numbers are not primes
    if not n & 1: 
        return False

    # range starts with 3 and only needs to go up 
    # the square root of n for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False

    return True


diagonal = [3,5,7,9]
primes = [True,True,True,False]
perc = 1
diag_size=3


while perc>0.1:
    #print('size: ' + str(diag_size) + ', perc: ' + str(perc) )
    diag_size = diag_size + 2
    diagonal = add_diagonal(diag_size,diagonal)
    primes = primes + [isprime(x) for x in diagonal[-4:]]
    
    perc = sum(primes)/(len(diagonal)+1)
    
print(diag_size)
