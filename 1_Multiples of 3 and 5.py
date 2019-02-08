multiple=[]
threshold=1000
i=1
testnum1=3*i
while testnum1 < threshold:
    multiple.append(testnum1)
    i+=1
    testnum1=3*i
j=1
testnum2=5*j
while testnum2 < threshold:
    if testnum2 not in multiple:
        multiple.append(testnum2)
    j+=1
    testnum2=5*j
print(sum(multiple))
    
    
