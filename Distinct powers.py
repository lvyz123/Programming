a=2;b=2;data_set=[]
import numpy as np
while a<=100:
    b=2
    while b<=100:
        data_set.append(a**b)
        b+=1
    a+=1
data_set_array=np.array(data_set)
dist_term=len(np.unique(data_set_array))
print(dist_term)
