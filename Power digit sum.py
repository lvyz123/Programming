i=16
import numpy as np
from math import *
digits=np.zeros(500)
digits[-5]=3;digits[-4]=2;digits[-3]=7;digits[-2]=6;digits[-1]=8
magnitude=5
while i<=1000:
    carry_over=0
    for j in range(magnitude):
        new_num=carry_over+digits[-j-1]*2
        digits[-j-1]=new_num%10
        carry_over=floor(new_num/10)
        if j==magnitude-1 and carry_over!=0:
            magnitude+=1
            digits[-j-2]=carry_over
    i+=1
print(sum(digits))
    
