threshold=4e6
fibonacci=[1,2]
sumselect=[2]
nextseq=fibonacci[-2]+fibonacci[-1]
while nextseq < threshold:
    fibonacci.append(nextseq)
    if nextseq%2==0:
        sumselect.append(nextseq)
    nextseq=fibonacci[-2]+fibonacci[-1]
print(sumselect)
print(sum(sumselect))
    
