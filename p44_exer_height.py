a=input("enter the height with space: ")
b=a.split()
print(b)
count=0
c=0
for height in b:
    count=count+1
print(count)
for i in b:
    c=c+int(i)
print(c)    

avg=c/count
print("avg height is",avg)




