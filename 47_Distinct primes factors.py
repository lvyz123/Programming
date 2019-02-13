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

first_num=644
prime_list=[2]
for a in range(3,int(first_num/2),2):
    if isprime(a)==True:
        prime_list.append(a)
four_consec=False
while four_consec==False:
    num_list=[first_num,first_num+1,first_num+2,first_num+3]
    if first_num%2==0:
        if isprime(first_num/2)==True:
            prime_list.append(first_num/2)
    this_four_consec=False
    for num_value in num_list:
        prime_factor=[]
        num=num_value
        for prime in prime_list:
            while num%prime==0:
                num/=prime
                prime_factor.append(prime)
        if len(list(set(prime_factor)))!=4:
            break
        if num_value==num_list[-1]:
            this_four_consec=True
    if this_four_consec==True:
        print(first_num)
        four_consec=True
    first_num+=1
