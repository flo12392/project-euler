
#28433×2**7830457

last_digits=10
range_max = 7830457
number = 28433

for i in range(1,range_max+1):
    number = number * 2
    number = number % 10**last_digits
    #print('i: ' + str(i) + ', number: ' + str(int(number)))


number+1
    