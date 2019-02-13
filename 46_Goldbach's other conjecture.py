from math import *

def isprime(n):
    prime_flag=True
    if n==1:
        return False
    for i in range(2,floor(sqrt(n))+1):
        if n%i==0:
            prime_flag=False
            break
    return prime_flag

odd_num=35
can_sum=True
while can_sum==True:
    comb_found=False
    if isprime(odd_num)==False:
        a_upper=floor(sqrt((odd_num-3)/2))
        for a in range(1,a_upper+1):
            if isprime(odd_num-2*a**2)==True:
                comb_found=True
                break
        if comb_found==False:
            can_sum=False
            print(odd_num)
    odd_num+=2
