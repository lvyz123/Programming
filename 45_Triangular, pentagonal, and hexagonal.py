p_n_rec=[]
h_n_rec=[]
for n in range(int(1e5)):
    t_n=n*(n+1)/2
    p_n=n*(3*n-1)/2
    p_n_rec.append(p_n)
    h_n=n*(2*n-1)
    h_n_rec.append(h_n)
    if (t_n in p_n_rec) and (t_n in h_n_rec) and t_n>40755:
        print(n,t_n)
        break
