def dig_value(digits):
    value=0;fifth_value=0
    for i in range(len(digits)):
        value+=digits[-i-1]*(10**i)
        fifth_value+=digits[i]**5
    return [value,fifth_value]

import numpy as np
from math import *
digits=np.zeros(6)
right_num=[]
for num in range(1,1000000):
    for j in range(len(digits)):
        digits[-j-1]=floor(num/(10**j))%10
    [value,fifth_value]=dig_value(digits)
    if value==fifth_value and value!=1:
        right_num.append(value)
print(sum(right_num))
