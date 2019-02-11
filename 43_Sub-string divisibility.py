from itertools import permutations
divisors=[2,3,5,7,11,13,17]
digit_perm=permutations(range(10))
sum_pand=0
for item in digit_perm:
    value=0
    if item[0]>0:
        for i,digit in enumerate(item):
            value+=digit*10**(9-i)
        str_value=str(value);i=1;divisible=True
        while i<=7:
            current_str=str_value[i:i+3]
            if int(current_str)%divisors[i-1]!=0:
                divisible=False
                break
            i+=1
        if divisible==True:
            sum_pand+=value
print(sum_pand)
