#positional we have to maintain sequence as well or it will be error
def greet(name, subject):
    print(f"Hi {name}")
    print(f"Do you teach {subject}?")
    #print(f"Are you from {dept} department?")

greet("Jenny","Python")




#deafult here default can also be changable
def greet(name, subject, dept="CS"):
    print(f"Hi {name}")
    print(f"Do you teach {subject}?")
    print(f"Are you from {dept} department?")
greet("Jenny","Python")
greet("Jenny","Python", "ME")

#default arguments should be provided after normal ones 
#also every argument should be fulfilled

#we cant miss anything in argument like if there are two then two should be there



#keywprd
def greet(name, subject):
    print(f"Hi {name}")
    print(f"Do you teach {subject}?")
    #print(f"Are you from {dept} department?")

greet(name="Jenny",subject="Python")





#arbitrary


def add(*numbers): #(5,7,9)
    c=0
    for i in numbers:
        c=c+i
    print(f"Sum is {c}")
add(5,7,9)
add(1,2,30,5,4,5,6)



























