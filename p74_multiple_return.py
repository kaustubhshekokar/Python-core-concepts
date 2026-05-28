"""import statistics
def mean_median_mode(list1):
    return [statistics.mean(list1),statistics.median(list1),statistics.mode(list1)]
    #return statistics.mean(list1),statistics.median(list1),statistics.mode(list1)
    #answer changes

print(mean_median_mode([3,4,5,6,7,8,9]))
a,b,c=mean_median_mode([3,4,5,6,7,8,9])
print(f"Mean is {a}\nMedian is {b}\nMode is {c}")
"""


def add(a,b):
    if a==0 & b==0:
        return "you have entered zero for both"
    else:
        return a+b
    
vr1=int(input("enter first variable:\n"))#enter 0
vr2=int(input("enter second variable:\n"))#enter 0
result=add(vr1,vr2)
print(result)






