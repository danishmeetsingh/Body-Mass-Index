height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

BMI = float(weight) / float(height) ** 2

if BMI < 18.5:
  print(f"Your BMI is {BMI}. You are Underweight")
elif BMI < 25:
  print(f"Your BMI is {BMI}. You have a Normal Weight")
elif BMI < 30:
  print(f"Your BMI is {BMI}. You are Overweight")
elif BMI < 35:
  print(f"Your BMI is {BMI}. You are Obese")
else:
  print(f"Your BMI is {BMI}. You are Clinically Obese")
  