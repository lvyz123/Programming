from math import *
p=12
max_sol=0
while p<1000:
    solutions=0
    skew_side=floor(p/2)
    while skew_side>p/3:
        straight_sum=p-skew_side
        for a in range(skew_side-1,ceil(sqrt(skew_side**2-(skew_side-1)**2))-1,-1):
            b=straight_sum-a
            if b>0 and sqrt(a**2+b**2)==skew_side:
                solutions+=1
        skew_side-=1
    if solutions>max_sol:
        max_sol=solutions
        p_max=p
    p+=1
print(max_sol,p_max)
