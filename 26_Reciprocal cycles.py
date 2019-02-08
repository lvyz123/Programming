def reci_cycle(str_input):
    str_input=str_input.lstrip('0.')
    for i in range(floor(len(str_input)/2)):
        if str_input[0:i]==str_input[i:2*i] and i>0:
            return i

from decimal import *
import numpy as np
from math import floor
cycle_rec=np.zeros(1000)
for d in range(2,1000):
    getcontext().prec=5000
    reci=Decimal(1)/Decimal(d)
    string_reci=str(reci)
    if reci_cycle(string_reci):
        cycle_rec[d]=reci_cycle(string_reci)
max_cycle=cycle_rec.argmax()
print(cycle_rec)
print(max_cycle)
