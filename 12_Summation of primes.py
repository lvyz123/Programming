testnum=2
primenum=[]
numlist=list(range(2,int(2e6)))
primeflag=1
sumprime=sum(primenum)
from math import *
while testnum<numlist[-1]:
    for i in range(2,ceil(sqrt(testnum))):
        if testnum%i==0:
            primeflag=0
            break
    if primeflag==1:
        primenum.append(testnum)
        sumprime+=testnum
        j=1
        while int(j*testnum)<=int(2e6):
            if j*testnum in numlist:
                numlist.remove(j*testnum)
            j+=1
    current_index=numlist.index(testnum)
    testnum=numlist[current_index+1]
    primeflag=1
print(sumprime)
