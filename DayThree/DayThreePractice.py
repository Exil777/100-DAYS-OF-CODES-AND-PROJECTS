# Check to see if a number input from the user is odd or even

#number_to_check = int(input("Enter a number you want to check: "))

#if number_to_check % 2 == 0:
    # print(f"number {number_to_check} is an even number")
# else:
    # print(f"number {number_to_check} is an odd number")
    


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




# Python Delivery pizza challenge
# small = $15, medium = $20, large = $25
# pepperoni small pizza = $2 large or medium = 3,  
# extra cheese = 1 
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

pizza_price = 0
if size == "s":
    pizza_price += 15
elif size == "m":
    pizza_price += 20
elif size == "l":
    pizza_price += 25
else:
    print("You type the wrong input")

if pepperoni == "y":
    if size == "s":
        pepperoni_price = 2
        pizza_price += pepperoni_price
    elif size == "m" or size == "l":
        pepperoni_price = 3
        pizza_price += pepperoni_price
    else: 
        print("You type the wrong input:")
elif pepperoni == "n":
    pizza_price = pizza_price
else:
    print("You type the wrong input")

if extra_cheese == "y":
    pizza_price += 1
elif extra_cheese == "n":
    pizza_price = pizza_price
else:
    print("You type the wrong input")

print(f"Your final bill is: {pizza_price}")
