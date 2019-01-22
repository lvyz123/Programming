import itertools
count=0
for i in range(10):
    perm_range=list(range(10))
    del perm_range[i]
    perm_rec=itertools.permutations(perm_range)
    perm_list=list(perm_rec)
    count+=len(perm_list)
    if count>=int(1e6):
        count-=len(perm_list)
        millionth=perm_list[int(1e6-count-1)]
        break
result=str(i)
for j in range(9):
    result+=str(millionth[j])
print(result)
