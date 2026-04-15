weight=input('what is weight?')
height=input('what is height?')

BMI=int(weight)//float(height) **2
print('BMI is',BMI)
if BMI<16:
    print("Under...")
elif 16<BMI<20:
    print("Under..")    
elif 20<BMI<24:
    print("Under..")
elif BMI>=40:
    print("obese")
else:
    print("Nope !!!!!!!")

print("Bye bye")                    