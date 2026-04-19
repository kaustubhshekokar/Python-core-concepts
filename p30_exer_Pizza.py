pizza=input("Which pizza do you want:")
bill=0

if pizza == "small":
    print("price is 100")
    bill=100
    
    pep1=input("Do you want peparoni:")
    if pep1=="yes":
        bill+=30
        print("your bill is ")
elif pizza == "medium":
    print("price is 150")
    bill=150

    pep3=input("Do you want peparoni:")
    if pep3=="yes":
        bill+=50
else:
    print("Large pizza is for 250")
    bill=250

    pep2=input("Do you want peparoni:")
    if pep2=="yes":
        bill+=50

cheese=input("Do you want cheese:")
if cheese=="yes":
    bill+=20
    print("your bill is",bill)  
