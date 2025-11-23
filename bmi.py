height = float(input(" what is your height ?"))
weight = float(input(" what is your weight ?"))
BMI = weight/(height/100)**2
print(" your bmi is ", BMI)
if BMI <= 18.4:
    print(" you are underweight, eat more !")
elif BMI <= 24.9:
    print(" you are at a healthy bmi, this is the only way to be!")
elif BMI <= 29.9:
    print("you are overweight go to the gym")
elif BMI <= 34.9:
    print(" you are severely overweight, get out of your house and excercise")
elif BMI <= 39.9:
    print(" you are obese, go lay on a hospital bed.")
else:
    print("you are severely obese, consider weight loss programs")
