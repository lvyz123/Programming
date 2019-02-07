from math import *

def isprime(a,b,n):
    quad_value=n**2+a*n+b
    prime_flag=True
    if quad_value>0:
        for i in range(2,floor(sqrt(quad_value))+1):
            if quad_value%i==0:
                prime_flag=False
                break
        return prime_flag
    else:
        return False

def quad_check(a,b):
    n=0
    prime_flag=True
    while prime_flag==True:
        prime_flag=isprime(a,b,n)
        n+=1
    num_prime=n-1
    return num_prime

max_num_prime=0
for a in range(1000):
    for b in range(1001):
        check_list=[quad_check(a,b),quad_check(-a,b),quad_check(a,-b),quad_check(-a,-b)]
        new_num_prime=max(check_list)
        prime_index=check_list.index(new_num_prime)
        if max_num_prime<new_num_prime:
            max_num_prime=new_num_prime
            a_max=a*(-1)**prime_index
            b_max=b*(-1)**floor(prime_index/2)
            product_ab=a_max*b_max
print(product_ab,max_num_prime)
