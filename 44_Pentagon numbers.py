pent_num_rec=[1]
D_rec=[]
pair_found=False
n=2
while pair_found==False:
    p_n=n*(3*n-1)/2
    D_rec=[p_n-item_1 for item_1 in pent_num_rec]
    pent_num_rec.append(p_n)
    D_qualified=list(set(D_rec).intersection(pent_num_rec))
    if D_qualified:
        for item_2 in D_qualified:
            S=2*pent_num_rec[-1]-item_2
            n_sum=n+1
            p_n_sum=p_n
            while p_n_sum<S:
                p_n_sum=n_sum*(3*n_sum-1)/2
                n_sum+=1
            if p_n_sum==S:
                pair_found=True
                print(n,item_2)
    n+=1
