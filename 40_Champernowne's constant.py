num=1
count=0
exponent=0
d=[]
while count<=int(1e6):
    count+=len(str(num))
    if count>=10**exponent:
        d.append(str(num)[-1-count+10**exponent])
        exponent+=1
    num+=1
product=1
for digit in d:
    product*=int(digit)
print(product)
