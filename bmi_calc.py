weight=float(input("Enter your weight (in kg): "))
height=float(input("Enter your height (in meters): "))
# bmi
bmi=weight/(height*height)
print(f"Your bmi is: {bmi} kg")
if bmi<18.5:
    print("You are underweight.")
elif bmi<25:
    print("You have a normal weight")
elif bmi<30:
    print("You are overweight.")
elif bmi<35:
    print("You are obese.")
else:
    print("You are clinically obese.")