height=int(input("print your height"))
bill = 0
if height>3:
    age=int(input("Enter your age:"))
    if age<12:
        bill=150
        print("bill will be 150")
    elif 12<age<18:
        bill=250
        print("bill will be 250")
    elif age>18:
        bill=500
        print("bill will be 500")
    else:
        print("not eligible")

    photo=input("do you want photo:")
    if photo =='yes' or photo =='Yes':
        bill+=50
        print("your bill is",bill) 
         
else:
    print("not eligible")
