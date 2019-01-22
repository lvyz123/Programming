fibonacci=[1,1]
length=2
while len(str(fibonacci[-1]))<1000:
    new_value=fibonacci[-2]+fibonacci[-1]
    fibonacci.append(new_value)
    length+=1
print(length)
