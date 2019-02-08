one_num=[0,3,3,5,4,4,3,5,5,4]
teen_num=[3,6,6,8,8,7,7,9,8,8]
ty_num=[6,6,5,5,5,7,6,6]
total_letter=0;i=0
import numpy as np
from math import *
below_hundred=np.zeros(100)
while i<1000:
    i+=1
    if i<10:
        below_hundred[i]=one_num[i]
        total_letter+=below_hundred[i]
    elif i<20:
        below_hundred[i]=teen_num[i-10]
        total_letter+=below_hundred[i]
    elif i<100:
        below_hundred[i]=ty_num[floor(i/10)-2]+one_num[i%10]
        total_letter+=below_hundred[i]
    elif i<1000:
        total_letter+=one_num[floor(i/100)]+7+below_hundred[i-floor(i/100)*100]
        if i%100!=0:
            total_letter+=3
    else:
        total_letter+=one_num[floor(i/1000)]+8
print(total_letter)
