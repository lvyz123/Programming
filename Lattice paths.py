import numpy as np
route=np.ones(20)
right_count=0;down_count=0
for i in range(20):
    p=(10-right_count)/(20-right_count-down_count)
    sample=np.random.binomial(1,p)
    if sample==1:
        right_count+=1
        route[i]=1
    else:
        down_count+=1
        route[i]=-1
print(route)
import math
nCr=math.factorial(40)/math.factorial(20)/math.factorial(20)
print(nCr)

