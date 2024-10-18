# Type casting 
name_of_user = input("What is your name: ")
length_of_name = str(len(name_of_user))
# type casting a int into a str so it may concatenate into a string
print("Number of letters in your name is " + length_of_name)


# Mathematical Operators
# PEMDAS = prioritize mathematical operations
# LR = left to right  
# ()
# **
# * OR / LR
# + OR - LR

height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / (height ** 2)
bmi = round(bmi, 1)

print(bmi)


# f-string
print(f"Your bmi is = {bmi}")