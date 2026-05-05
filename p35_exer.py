
#pay the bill ame

import random

a=input("enter the names with space")
b=a.split(" ")
print(b)

len=len(b)
biller=random.randint(0,len-1)
#can do it by random.choice...directly
print(f"{b[biller]} will pay th bill")

