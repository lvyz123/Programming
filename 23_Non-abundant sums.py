from math import *

def abun(n):
    divisor=[]
    for i in range(1,floor(n/2)+1):
        if n%i==0:
            divisor.append(i)
    sum_div=sum(divisor)
    if sum_div>n:
        abun_flag=1
    else:
        abun_flag=0
    return abun_flag

abun_rec=[]
abun_sum_rec=[]
for j in range(1,28124):
    if abun(j)==1:
        abun_rec.append(j)
print(abun_rec)
for k in abun_rec:
    abun_start=abun_rec.index(k)
    for l in abun_rec[abun_start:]:
        abun_sum=k+l
        if abun_sum<=28123 and abun_sum not in abun_sum_rec:
            abun_sum_rec.append(abun_sum)
abun_total=sum(abun_sum_rec)
sum_total=sum(range(28124))
solution=sum_total-abun_total
