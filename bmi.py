height = float(input(" what is your height ?"))
weight = float(input(" what is your weight ?"))
BMI = weight/(height/100)**2
print(" your bmi is ", BMI)
if BMI <= 18.4:
    print(" you are underweight !")
elif BMI <= 24.9:
    print(" you are at a healthy bmi !")
elif BMI <= 29.9:
    print("you are overweight")
elif BMI <= 34.9:
    print(" you are severely overweight")
elif BMI <= 39.9:
    print(" you are obese, sorry.")
else:
    print("you are severely obese")
