i=j=999
flag=1
digit=6
palindrome=[]
import math
while flag==1:
    product=i*j
    if product<1e5 and digit==6:
        digit=5
    if product>1e5 and digit==5:
        digit=6
    minunit=product%10
    maxunit=math.floor(product/(10**(digit-1)))
    i-=1
    if i<100:
        j-=1
        i=j
    if minunit==maxunit:
        minunit2=math.floor(product/10)%10
        maxunit2=math.floor(product/(10**(digit-2)))%10
        if minunit2==maxunit2:
            if digit==6:
                minunit3=math.floor(product/100)%10
                maxunit3=math.floor(product/(10**(digit-3)))%10
                if minunit3==maxunit3:
                    palindrome.append(product)
            else:
                palindrome.append(product)
    if j<100:
        flag=0
        break
print("The largest palindrome product is "+str(max(palindrome)))
