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

num=11
trunc_prime=[]
while len(trunc_prime)<11:
    num_str=str(num)
    trunc_prime_flag=True
    if isprime(num)==True and (int(j)%2==1 for j in num_str):
        for k in range(len(num_str)-1):
            num_str_left=num_str[k+1:];num_left=int(num_str_left)
            num_str_right=num_str[:-k-1];num_right=int(num_str_right)
            if isprime(num_left)==False or isprime(num_right)==False:
                trunc_prime_flag=False
                break
    else:
        trunc_prime_flag=False
    if trunc_prime_flag==True:
        trunc_prime.append(num)
    num+=1
print(sum(trunc_prime))
