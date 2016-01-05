#Python3

weight = int(input('Enter the weight(in pounds): '))

height = int(input('Enter the height(in inch): '))

BMI = (weight*0.45359237)/(height*0.0254)**2

print('BMI: ', BMI)

if BMI < 18.5:
    print("Underweight")
elif BMI < 25.0:
    print("Normal")
elif BMI < 30.0:
    print("Overweight")
else:
    print("Obese")

