# Tip Calculator Project
# A calculator that calculate the amount of tips that need to giving base on the user uption and calculate the total amount each person have to pay base of the number the check is being split in bettwen 

print("Welcome to the tip calculator!")
bill_amount = float(input("What was the bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
bill_splits = int(input("How many people to slip the bill? "))

tips_amount = bill_amount * (tip / 100)

amount_each_person_pay = (bill_amount + tips_amount) / bill_splits
amount_each_person_pay = round(amount_each_person_pay, 2)
print(f"Each person should pay: ${amount_each_person_pay}")