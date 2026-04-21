num= [10, 0, -1, 7, 8, 10, -67]
print(len(num))
print(num[0:3])
print(num.sort())#here it will give none
num.sort()
print(num)#here it will sort
num.reverse()
print(num)
num.append(45)#will be added at end
print(num)
num.insert(2,45)
print(num)
num.extend([45,46,47,48])#added at the end 
num[1]=45#add at spcific pos
print(num)
num[1:4]=[45,46,47]
print(num)
num.remove(0)
print(num)
print(num.pop())
print(num)
print(num.pop(5))
