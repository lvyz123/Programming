from math import *
value=10
value_rec=[]
for num_digit in range(2,8):
    if num_digit==7:
        max_num=factorial(9)*7
    else:
        max_num=10**num_digit
    while value<max_num:
        digits=[0]*num_digit
        sum_fact=0
        for i in range(num_digit):
            digits[-i-1]=floor(value/10**i)%10
            sum_fact+=factorial(digits[-i-1])
        if sum_fact==value:
            value_rec.append(sum_fact)
        value+=1
print(sum(value_rec))
