num=11
last_ten_digits='0405071317'
while num<=1000:
    value=int(last_ten_digits)
    value+=num**num
    last_ten_digits=str(value)[-10:]
    num+=1
print(last_ten_digits)
