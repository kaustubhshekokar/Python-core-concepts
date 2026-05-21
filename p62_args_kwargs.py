"""def add(*numbers):
    c=0
    for i in numbers:
        c +=i
    print(f"sum is {c}")    

add(1,2)
add(1,3,4,5)
add(3,3,3)



def add1(*numbers,name):
    c=0
    print(numbers)
    print(name)
    #for i in numbers:
    #    c +=i
    #print(f"sum is {c}")    

add1(1,2,name="Kaustubh")
#add(1,3,4,5)
#add(3,3,3)

"""
#kwargs
def info_person(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
    
info_person(name="Ram",age=30,dept="CSE")
info_person(name="Sam",dept="CSE")


def info_person(*args,**kwargs):
    for key,value in kwargs.items():
        print(key,value)
    print(args)
info_person(4,5,6,name="Ram",age=30,dept="CSE")
info_person(6,6,6,name="Sam",dept="CSE")


def mul(*args):
    c=1
    for i in args:
        c=c*i
    print(f"the product is {c}")    
mul(2,3,-6,8)
mul(2,3,)