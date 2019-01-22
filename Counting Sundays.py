year=1900
month=1
day=1
week=1
sunday_first=0
while year<=2000:
    if year%4==0 and year%100!=0:
        leap_yr=1
    elif year%400==0:
        leap_yr=1
    else:
        leap_yr=0
    while month<=12:
        if month in [4,6,9,11]:
            day_end=30
        elif month==2:
            if leap_yr==1:
                day_end=29
            else:
                day_end=28
        else:
            day_end=31
        while day<=day_end:
            if day==1 and week==7 and year!=1900:
                sunday_first+=1
            day+=1;week+=1
            if week>7:
                week=1
        day=1;month+=1
    month=1;year+=1
print(sunday_first)
            
    
