from math import *
from itertools import permutations

def isprime(n):
    prime_flag=True
    if n==1:
        return False
    for i in range(2,floor(sqrt(n))+1):
        if n%i==0:
            prime_flag=False
            break
    return prime_flag

num_digit=4
max_pand_prime=2143
while num_digit<=9:
    digit_perm=permutations(range(1,num_digit+1))
    for item_1 in digit_perm:
        value=0
        for i,digit in enumerate(item_1):
            value+=digit*10**(num_digit-i-1)
        if item_1[-1] not in [2,4,5,6,8]:
            prime_flag=isprime(value)
            if prime_flag==True and max_pand_prime<value:
                max_pand_prime=value
    num_digit+=1
print(max_pand_prime)
