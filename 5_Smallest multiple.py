num=2521
eliminated=0
while num<1e50:
    for i in range(2,20):
        if num%i!=0:
            eliminated=1
            break
    if eliminated==0:
        print(num)
        break
    else:
        num+=1
        eliminated=0
