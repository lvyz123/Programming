num=3
count=2
import math
while count<=10001:
    num+=1
    flag=1
    for i in range(2,math.floor(num/2)):
        if num%i==0:
            flag=0
            break
    if flag==1:
        count+=1
print(num)
