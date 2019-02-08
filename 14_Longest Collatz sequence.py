test_num=int(1e6-1)
max_len=0
while test_num>1:
    len_chain=1
    n=test_num
    while n>1:
        if n%2==0:
            n=n/2
        else:
            n=3*n+1
        len_chain+=1
    if max_len<len_chain:
        max_len=len_chain
        longest_num=test_num
    test_num-=1
print(max_len)
print(longest_num)
