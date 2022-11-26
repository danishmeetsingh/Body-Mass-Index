height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

BMI_value= float(weight) / float(height) ** 2
BMI = round(BMI_value, 3)
print(str(BMI) + " kg/m²")