tuple1=(12,4,-7,'jenny',True)
tuple2=(5,)
#tuple2=(5)
print(tuple1)
print(tuple1[1])
print(type(tuple1))
print(type(tuple2))#without comma its only int
#tuples are immutable, we cannot change any value or anything
#tuple1[0]=4#no 
print(tuple1)
#slicing like lists is also allowed
tuple3=(tuple2,tuple1)#nesting is possible
tuple4 = tuple1 + tuple2#here it is cancatenation 
print(tuple3)
print(tuple4)
print(len(tuple3))
print(len(tuple4))
#mostly similar to lists like min max count index fns
list1=[2,3,4]#can convert list into tuple
print(tuple(list1))

tuple5=(10,)*5
print(tuple5)




