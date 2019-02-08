from math import *
prime_sum=2

def isprime(n):
    prime_flag=True
    for i in range(3,floor(sqrt(n))+1,2):
        if n%i==0:
            prime_flag=False
            break
    return prime_flag

for num in range(3,int(2e6),2):
    prime_flag=isprime(num)
    if prime_flag==True:
        prime_sum+=num
print(prime_sum)
