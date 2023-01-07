def calculate_bmi(weight, height):
  bmi = weight / (height ** 2)
  return bmi

# Prompt the user to select the unit type
unit_type = input("Enter 'm' for metric units or 'i' for imperial units: ")

if unit_type == "m":
  weight = float(input("Enter your weight in kilograms: "))
  height = float(input("Enter your height in meters: "))
elif unit_type == "i":
  weight = float(input("Enter your weight in pounds: "))
  feet = float(input("Enter your height in feet: "))
  inches = float(input("Enter your remaining height in inches: "))
  # Convert pounds to kilograms and feet and inches to meters
  weight = weight / 2.2
  height = (feet * 12 + inches) / 39.37
else:
  print("Invalid unit type. Please enter 'm' for metric or 'i' for imperial.")
  exit()

bmi = calculate_bmi(weight, height)
print(f"Your BMI is {bmi:.2f}.")

# Save the result to a file
with open("results.txt", "w") as file:
  file.write(f"Your BMI is {bmi:.2f}.")
