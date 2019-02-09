import numpy as np
max_pand_num=918273645
num=91
while num<10000:
    multiply=2
    str_num=str(num)
    str_9_digit=str_num
    while len(str_9_digit)<9:
        product=num*multiply
        str_9_digit+=str(product)
        multiply+=1
    str_9_digit=str_9_digit[:9]
    list_9_digit=[str_9_digit[i] for i in range(9)]
    if int(str_9_digit)>max_pand_num and len(list(set(list_9_digit)))==9 and '0' not in list_9_digit:
        max_pand_num=int(str_9_digit)
    if num==10**len(str_num)-1:
        num=918*10**(len(str_num)-2)
    else:
        num+=1
print(max_pand_num)
