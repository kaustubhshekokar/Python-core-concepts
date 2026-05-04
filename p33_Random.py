import random

a=random.randint(1,7)#so it gives anything between the range
print(a)

a=random.randrange(1,3)#here last no. is not included
print(a)

a=random.random()#any float value
print(a)
a=random.uniform(2,5)
print(a)
#a=random.choice(l)
print(a)
l=[2,10,-40,3,94]
random.shuffle(l)
print(l)



