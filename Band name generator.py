Weight = int(input("Enter your weight in Kg: "))
Height = float(input("Enter your height in Mtr: "))
BMI = Weight/Height ** 2
print(f"Your BMI is: {int(BMI)} ")

if BMI<=18.5:
    print("You are underweight!")
elif BMI<=25:
    print("You are normal weight!")
elif BMI<=30:
    print("You are over weight!")
elif BMI<=35:
    print("You are obese!")
else:
    print("You are clinically obese!")
