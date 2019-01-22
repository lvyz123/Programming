from math import *

def d(n):
    divisor=[]
    for i in range(1,floor(n/2)+1):
        if n%i==0:
            divisor.append(i)
    sum_div=sum(divisor)
    return sum_div

sum_div_rec=[0]
amic_pair=[]
for j in range(1,10001):
    sum_div=d(j)
    sum_div_rec.append(sum_div)
    if len(sum_div_rec)>sum_div:
        if j==d(sum_div) and j!=sum_div:
            amic_pair.append(j)
            amic_pair.append(sum_div)
print(sum(amic_pair))
