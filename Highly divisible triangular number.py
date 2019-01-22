nat_num=1
nat_sum=1
factor_num=1
from math import *
while factor_num<=500:
    divisor=[]
    nat_num+=1
    nat_sum+=nat_num
    for i in range(1,ceil(nat_sum/2)+1):
        if nat_sum%i==0:
            divisor.append(i)
    factor_num=len(divisor)
print(nat_sum)
