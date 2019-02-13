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

for small_num in range(1000,9999-6660):
    if isprime(small_num)==True:
        mid_num=small_num+3330
        large_num=mid_num+3330
        if isprime(mid_num)==True and isprime(large_num)==True:
            small_set=list(set(str(small_num)))
            mid_set=list(set(str(mid_num)))
            large_set=list(set(str(large_num)))
            if small_set==mid_set==large_set:
                print(small_num,mid_num,large_num)
