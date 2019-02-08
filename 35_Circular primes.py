from math import *

def isprime(n):
    prime_flag=True
    for i in range(2,floor(sqrt(n))+1):
        if n%i==0:
            prime_flag=False
            break
    return prime_flag

untested_num=[]
circ_prime_count=1
for j in range(3,int(1e6),2):
    untested_num.append(j)
num=untested_num[0]
while num!=untested_num[-1]:
    untested_num.remove(num)
    if isprime(num)==True:
        num_digits=len(str(num))
        is_circ_prime=True
        for k in range(num_digits):
            if num in untested_num:
                untested_num.remove(num)
            next_str=str(num)+str(num)[0]
            next_str=next_str[1:]
            num=int(next_str)
            if next_str[0]=='0' or isprime(num)==False:
                is_circ_prime=False
                break
        if is_circ_prime==True:
            circ_prime_count+=num_digits
    num=untested_num[0]
print(circ_prime_count)
