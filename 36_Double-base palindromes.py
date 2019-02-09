from math import *
sum_palin=0
for num in range(1,int(1e6)):
    num_10_str=str(num)
    base10_palin=True;l=0
    while l<=floor(len(num_10_str)/2)-1:
        if num_10_str[l]!=num_10_str[-l-1]:
            base10_palin=False
            break
        l+=1
    if base10_palin==True:
        num_2_str=bin(num)[2:]
    else:
        continue
    base2_palin=True;k=0
    while k<=floor(len(num_2_str)/2)-1:
        if num_2_str[k]!=num_2_str[-k-1]:
            base2_palin=False
            break
        k+=1
    if base2_palin==True:
        sum_palin+=num
print(sum_palin)
