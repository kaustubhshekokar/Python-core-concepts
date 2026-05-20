#positional we have to maintain sequence as well or it will be error
def greet(name, subject):
    print(f"Hi {name}")
    print(f"Do you teach {subject}?")
    #print(f"Are you from {dept} department?")

greet("Jenny","Python")




#deafult here default can also be changable
def greet(name, subject, dept="cs"):
    print(f"Hi {name}")
    print(f"Do you teach {subject}?")
    print(f"Are you from {dept} department?")
greet("Jenny","Python")
greet("Jenny","Python", "ME")






#keywprd
def greet(name, subject):
    print(f"Hi {name}")
    print(f"Do you teach {subject}?")
    #print(f"Are you from {dept} department?")

greet(name="Jenny",subject="Python")





#arbitrary





























