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

prime_list=[2]
for num in range(3,int(1e6),2):
    if isprime(num)==True:
        prime_list.append(num)
max_len_sum=21
total_sum_prime=sum(prime_list)
for index,prime in enumerate(prime_list):
    sum_prime=total_sum_prime
    minus_index=len(prime_list)-1
    while sum_prime>=int(1e6) or isprime(sum_prime)==False:
        sum_prime-=prime_list[minus_index]
        minus_index-=1
    len_sum=minus_index-index+1
    if len_sum>max_len_sum:
        max_len_sum=len_sum
        max_sum_prime=sum_prime
        start_index=index
    total_sum_prime-=prime
print(max_len_sum,max_sum_prime,start_index)    
