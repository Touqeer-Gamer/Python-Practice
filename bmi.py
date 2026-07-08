Weight = float(input("Enter Your Weight (in KGs) : "))
Height = float(input("Enter Your Heght (ine meters) : "))

print("Your Weight : ",Weight)
print("Your Height : ",Height)
bmi = Weight/Height**2
print(f"BMI =  {bmi:.2f}")