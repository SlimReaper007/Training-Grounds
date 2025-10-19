h = float((input("Enter your height in meters: ")))
w = float((input("Enter your weight in kilograms: ")))

bmi = w / (h ** 2) 

if bmi < 18.5:
    print("Your BMI is", round(bmi, 2), "which means you are underweight.")
elif 18.5 <= bmi < 25:
    print("Your BMI is", round(bmi, 2), "which means you have a normal weight.")
elif 25 <= bmi < 30:
    print("Your BMI is", round(bmi, 2), "which means you are overweight.")
else:
    print("Your BMI is", round(bmi, 2), "which means you are obese.")   