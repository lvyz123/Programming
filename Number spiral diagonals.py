diag_sum=0;
for i in range(1,1003,2):
    pos_diag1=i**2
    diag_sum+=pos_diag1
    if i>1:
        neg_diag1=pos_diag1-2*(i-1)
        diag_sum+=neg_diag1
        neg_diag2=pos_diag1-(i-1)
        diag_sum+=neg_diag2
        pos_diag2=pos_diag1-3*(i-1)
        diag_sum+=pos_diag2
print(diag_sum)
