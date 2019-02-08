import numpy as np
from itertools import combinations
coins=[1,2,5,10,20,50,100,200]
coin_combination=[0]*len(coins)
coin_combination[0]=1
for i in range(1,len(coins)):
    if coins[i]>=2*coins[i-1]:
        remain_value=coins[i]-2*coins[i-1]
        coin_combination[i]=coin_combination[i-1]*(coin_combination[i-1]+1)/2
        if remain_value in coins:
            coin_combination[i]*=coin_combination[coins.index(remain_value)]
    coin_combination[i]+=1
print(coin_combination[-1])
