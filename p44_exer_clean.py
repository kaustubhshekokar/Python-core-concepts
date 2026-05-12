heights=input("enter the heights with spaace")
height_list=heights.split()
print(height_list)
count=0
sum=0
for height in height_list:
    count=count+1
print(count)
for i in range(count):
    height_list[i]=int(height_list[i])


for m in height_list:
    sum+= m
avg=sum/count
print("avg height is",avg)    







