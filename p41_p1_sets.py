set1= {10,1,True,89,90,'jenny'}
print(set1)#here True and 1 are same so only one output
#print(set1[2])#slicing and indexing is not allowed
set2={}
set3=set()#empty set
print(type(set2))
print(type(set1))
print(type(set3))
print(len(set1))
set1.add(99)#one at a time 
set1.remove(90)#if not present then keyerror
print(set1)
#set1.clear()
print(set1.pop())



