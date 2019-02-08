from itertools import permutations
import numpy as np
rec_product=[]
total='123456789'
equal_left=list(permutations(total,5))
for comb in equal_left:
    leftover=''.join(list(set(total)-set(comb)))
    equal_right=list(permutations(leftover))
    for index,comb1 in enumerate(equal_right):
        equal_right[index]=''.join(comb1)
    product1=(10*int(comb[0])+int(comb[1]))*(100*int(comb[2])+10*int(comb[3])+int(comb[4]))
    product2=int(comb[0])*(1000*int(comb[1])+100*int(comb[2])+10*int(comb[3])+int(comb[4]))
    if str(product1) in equal_right:
        rec_product.append(product1)
    elif str(product2) in equal_right:
        rec_product.append(product2)
uniq_product=np.unique(np.array(rec_product))
print(sum(uniq_product))
