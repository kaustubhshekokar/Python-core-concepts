height=int(input("Enter the height"))

if height>3:
    print("can ride")
    age=int(input("enter your age"))
    if age<12:
        print("pay 150 rs")
    elif age<18:
        print("pay 225 rs")   
    else:
        print("pay 300 rs")

else:
    print("Nope")            
print("boye bye")