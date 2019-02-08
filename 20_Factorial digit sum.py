from math import *
import numpy as np
dividend=value=factorial(100)
i=0
sum_digits=0
str_value=str(value)
for j in range(len(str_value)):
    sum_digits+=int(str_value[j])
print(sum_digits)
#digits=np.zeros(200)
#while dividend>=1:
    #dividend=value/pow(10,i)
    #digits[-i-1]=floor(dividend)%10
    #i+=1
#print(sum(digits))
