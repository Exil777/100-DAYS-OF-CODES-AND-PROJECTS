# Check to see if a number input from the user is odd or even

number_to_check = int(input("Enter a number you want to check: "))

if number_to_check % 2 == 0:
    print(f"number {number_to_check} is an even number")
else:
    print(f"number {number_to_check} is an odd number")
    


# BMI calculator with interpretation
# If the bmi is under 18.5 (not including), print out "underweight"

#If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"

#If the bmi is 25 (including) or over, print out "overweight"
weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")