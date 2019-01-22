num=1
sumsquare=squaresum=sum=0
while num<=100:
    squaresum+=num**2
    sum+=num
    num+=1
sumsquare=sum**2
diff=sumsquare-squaresum
print(diff)
    
