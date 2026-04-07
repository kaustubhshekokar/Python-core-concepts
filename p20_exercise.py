weight=input('what is weight?')
height=input('what is height?')

BMI=int(weight)/(float(height) **2)
print('BMI is',BMI)

# BMI Calculator

# Taking input
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

# BMI formula
bmi = weight / (height ** 2)

# Output BMI
print("Your BMI is:", round(bmi, 2))

# Category
if bmi < 18.5:
    print("Category: Underweight")
elif 18.5 <= bmi < 24.9:
    print("Category: Normal weight")
elif 25 <= bmi < 29.9:
    print("Category: Overweight")
else:
    print("Category: Obese")