#break



"""count=1
while count<=10:
    print(count)
    count+=1
    if count==7:
        break
    print("hi")
print("out of the loop")    
"""
"""
list1=["hi","hello","welcome"]
names=["ram","sam","dam"]
for item in list1:
    for name in names:
        print(item,name)
        if item=="hello" and name=="ram":
            break
    print("out from inner loop")    
print("out from loop")
"""

#continue

count=1
while count<=10:
    print(count)
    count+=1
    if count==7:
        continue
    print("hi")
print("out of the loop") 

for i in range(1,11):
    if i==7:
        continue
    else:
        print(i)



#pass
for i in range(1,11):
    if i==7:
        pass
    else:
        print(i)











