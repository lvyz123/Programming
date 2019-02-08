from math import *
from fractions import Fraction
denominator_product=1
numerator_product=1
for denominator in range(99,9,-1):
    ind_dig_den=denominator%10
    ten_dig_den=floor(denominator/10)
    if denominator%10==0:
        continue
    for numerator in range(denominator-1,9,-1):
        new_denominator=0
        old_value=numerator/denominator
        ind_dig_num=numerator%10
        ten_dig_num=floor(numerator/10)
        if ind_dig_num==ind_dig_den:
            new_denominator=ten_dig_den
            new_numerator=ten_dig_num
        elif ten_dig_num==ten_dig_den:
            new_denominator=ind_dig_den
            new_numerator=ind_dig_num
        elif ind_dig_num==ten_dig_den:
            new_denominator=ind_dig_den
            new_numerator=ten_dig_num
        elif ten_dig_num==ind_dig_den:
            new_denominator=ten_dig_den
            new_numerator=ind_dig_num
        if new_denominator!=0:
            new_value=new_numerator/new_denominator
            if new_value==old_value:
                denominator_product*=new_denominator
                numerator_product*=new_numerator
final_result=Fraction(numerator_product,denominator_product).denominator
print(final_result)
