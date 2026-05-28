year=int(input("enter the year : "))
month=int(input("enter the month's num : "))

def daycheck(year,month):
    if year%4==0:
        if month in [1,3,5,7,8,10,12]:
            return "no. of days are 31"
        elif month in [4,6,9,11]:
            return "no. of days are 30"
        else:
            return "no. of days are 28"
    else:
        if month in [1,3,5,7,8,10,12]:
            return "no. of days are 31"
        elif month in [4,6,9,11]:
            return "no. of days are 30"
        else:
            return "no. of days are 29"
            
 
days=daycheck(year,month)
print(days)   





























