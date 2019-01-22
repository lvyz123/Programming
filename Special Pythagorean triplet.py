a=1;b=1
value=1
while value!=0:
    b+=1
    if b>=1000-a:
        a+=1;b=a
    c=1000-a-b
    value=pow(a,2)+pow(b,2)-pow(c,2)
print(a*b*c)

