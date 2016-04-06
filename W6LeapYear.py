def FindLeapYear(year):
    if (year%4 == 0) and (year%100 !=0 or year%400==0):
        res="LeapYear"
    else:
        res="normal"
    return res