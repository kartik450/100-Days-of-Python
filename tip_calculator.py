x=float(input("Enter your total bill: "))
y=int(input("Enter how much percent tip you want to give?: "))
z=int(input("Enter number of persons: "))

print(f"Total bill= {((y/100)*x)+x}")
print(f"Each person should pay: {(((y/100)*x)+x)/z}")