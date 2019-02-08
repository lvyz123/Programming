testnum=600851475143
primenum=[]
primeproduct=1
primeflag=1
j=3
for i in range(3,round(testnum/2),2):
    if testnum%i==0:
        for j in range(3,i,2):
            if i%j==0 and i!=j:
                primeflag=0
                break
        if primeflag==1:
            primenum.append(i)
            primeproduct*=i
            if primeproduct==testnum:
                break
print(primenum[-1])
